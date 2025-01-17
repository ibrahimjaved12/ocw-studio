""" YouTube API interface"""
import http
import logging
import re
import time
from io import BytesIO
from urllib.parse import urljoin

from django.conf import settings
from django.db.models import Q
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload
from mitol.mail.api import get_message_sender
from smart_open.s3 import Reader

from content_sync.constants import VERSION_DRAFT, VERSION_LIVE
from main.s3_utils import get_boto3_client
from main.utils import truncate_words
from videos.constants import (
    DESTINATION_YOUTUBE,
    YT_MAX_LENGTH_DESCRIPTION,
    YT_MAX_LENGTH_TITLE,
)
from videos.messages import YouTubeUploadFailureMessage, YouTubeUploadSuccessMessage
from videos.models import VideoFile
from websites.api import is_ocw_site
from websites.constants import RESOURCE_TYPE_VIDEO
from websites.models import Website, WebsiteContent
from websites.utils import get_dict_field, get_dict_query_field


log = logging.getLogger(__name__)

# Quota errors should contain the following
API_QUOTA_ERROR_MSG = "quota"
CAPTION_UPLOAD_NAME = "ocw_captions_upload"


class YouTubeUploadException(Exception):
    """Custom exception for YouTube uploads"""


def is_youtube_enabled() -> bool:
    """ Returns True if youtube is enabled """
    return (
        settings.YT_ACCESS_TOKEN
        and settings.YT_REFRESH_TOKEN
        and settings.YT_CLIENT_ID
        and settings.YT_CLIENT_SECRET
        and settings.YT_PROJECT_ID
    )


def mail_youtube_upload_failure(video_file: VideoFile):
    """Notify collaborators that a youtube upload failed"""
    with get_message_sender(YouTubeUploadFailureMessage) as sender:
        website = video_file.video.website
        for collaborator in website.collaborators:
            sender.build_and_send_message(
                collaborator,
                {
                    "site": {
                        "title": website.title,
                        "url": urljoin(
                            settings.SITE_BASE_URL,
                            f"sites/{website.name}",
                        ),
                    },
                    "video": {"filename": video_file.video.source_key.split("/")[-1]},
                },
            )


def mail_youtube_upload_success(video_file: VideoFile):
    """Notify collaborators that a youtube upload succeeded"""
    with get_message_sender(YouTubeUploadSuccessMessage) as sender:
        website = video_file.video.website
        for collaborator in website.collaborators:
            sender.build_and_send_message(
                collaborator,
                {
                    "site": {
                        "title": website.title,
                        "url": urljoin(
                            settings.SITE_BASE_URL,
                            f"sites/{website.name}",
                        ),
                    },
                    "video": {
                        "filename": video_file.video.source_key.split("/")[-1],
                        "url": f"https://www.youtube.com/watch?v={video_file.destination_id}",
                    },
                },
            )


def resumable_upload(request, max_retries=10):
    """
    Upload a video to YouTube and resume on failure up to 10 times, adapted from YouTube API example.
    To use resumable media you must use a MediaFileUpload object and flag it as a resumable upload.
    You then repeatedly call next_chunk() on the googleapiclient.http.HttpRequest object until the
    upload is complete.

    Args:
        request(googleapiclient.http.HttpRequest): The Youtube API execute request to process
        max_retries(int): Maximum # of times to retry an upload (default 10)

    Returns:
        dict: The YouTube API response
    """
    response = None
    error = None

    retry = 0
    retry_exceptions = (OSError, http.client.HTTPException)
    retry_statuses = [500, 502, 503, 504]

    while response is None:
        try:
            _, response = request.next_chunk()
            if response is not None and "id" not in response:
                raise YouTubeUploadException("YouTube upload failed: %s" % response)
        except HttpError as e:
            if e.resp.status in retry_statuses:
                error = e
            else:
                raise
        except retry_exceptions as e:
            error = e

        if error is not None:
            retry += 1
            if retry > max_retries:
                log.error("Final upload failure")
                raise YouTubeUploadException(
                    "Retried YouTube upload 10x, giving up"
                ) from error
            sleep_time = 2 ** retry
            time.sleep(sleep_time)

    return response


def strip_bad_chars(txt):
    """
    Remove any characters forbidden by Youtube (<, >) from text

    Args:
        txt(str): Text to remove characters from.

    Returns:
        str: Text without bad characters
    """
    return re.sub("<|>", "", txt)


class YouTubeApi:
    """
    Class interface to YouTube API calls
    """

    client = None
    s3 = None

    def __init__(self):
        """
        Generate an authorized YouTube API client and S3 client
        """
        credentials = Credentials(
            settings.YT_ACCESS_TOKEN,
            token_uri="https://accounts.google.com/o/oauth2/token",
            client_id=settings.YT_CLIENT_ID,
            client_secret=settings.YT_CLIENT_SECRET,
            refresh_token=settings.YT_REFRESH_TOKEN,
        )
        self.client = build("youtube", "v3", credentials=credentials)
        self.s3 = get_boto3_client("s3")

    def video_status(self, video_id):
        """
        Checks the  status of a video. 'processed' = ready for viewing.

        Args:
            video_id(str): YouTube video id

        Returns:
            str: status of the YouTube video

        """
        results = self.client.videos().list(part="status", id=video_id).execute()
        return results["items"][0]["status"]["uploadStatus"]

    def upload_video(
        self, videofile: VideoFile, privacy="unlisted", notify_subscribers=False
    ):
        """
        Transfer the video's original video file from S3 to YouTube.
        The YT account must be validated for videos > 15 minutes long:
        https://www.youtube.com/verify

        Args:
            video(Video): The Video object whose original source file will be uploaded'
            privacy(str): The privacy level to set the YouTube video to.
            notify_subscribers(bool): whether subscribers should be notified

        Returns:
            dict: YouTube API response

        """
        original_name = videofile.video.source_key.split("/")[-1]
        request_body = dict(
            snippet=dict(
                title=truncate_words(
                    strip_bad_chars(original_name), YT_MAX_LENGTH_TITLE
                ),
                description="",
                categoryId=settings.YT_CATEGORY_ID,
            ),
            status=dict(privacyStatus=privacy),
        )

        with Reader(settings.AWS_STORAGE_BUCKET_NAME, videofile.s3_key) as s3_stream:
            request = self.client.videos().insert(
                part=",".join(request_body.keys()),
                body=request_body,
                notifySubscribers=notify_subscribers,
                media_body=MediaIoBaseUpload(
                    s3_stream, mimetype="video/*", chunksize=-1, resumable=True
                ),
            )

        response = resumable_upload(request)
        return response

    def update_privacy(self, youtube_id: str, privacy: str):
        """Update the privacy level of a video"""
        self.client.videos().update(
            part="status",
            body={
                "id": youtube_id,
                "status": {"privacyStatus": privacy, "embeddable": True},
            },
        ).execute()

    def update_captions(self, resource: WebsiteContent, youtube_id: str):
        """Update captions for video"""

        videofile = VideoFile.objects.filter(
            destination=DESTINATION_YOUTUBE,
            destination_id=youtube_id,
            video__website=resource.website,
        ).last()

        if not videofile or not videofile.video.webvtt_transcript_file:
            return

        content = videofile.video.webvtt_transcript_file.open(mode="rb").read()

        media_body = MediaIoBaseUpload(
            BytesIO(content), mimetype="text/vtt", chunksize=-1, resumable=True
        )

        existing_captions = (
            self.client.captions().list(part="snippet", videoId=youtube_id).execute()
        )

        existing_captions = existing_captions.get("items", [])
        existing_captions = list(
            filter(
                lambda caption_file: caption_file.get("snippet", {}).get("name")
                == CAPTION_UPLOAD_NAME,
                existing_captions,
            )
        )

        if existing_captions:
            self.client.captions().update(
                part="snippet",
                body={"id": existing_captions[0].get("id")},
                media_body=media_body,
            ).execute()
        else:
            self.client.captions().insert(
                part="snippet",
                sync=False,
                body={
                    "snippet": {
                        "language": "en",
                        "name": CAPTION_UPLOAD_NAME,
                        "videoId": youtube_id,
                    }
                },
                media_body=media_body,
            ).execute()

    def update_video(self, resource: WebsiteContent, privacy=None):
        """
        Update a video's metadata based on a WebsiteContent object that is assumed to have certain fields.
        """
        metadata = resource.metadata
        description = get_dict_field(metadata, settings.YT_FIELD_DESCRIPTION)
        speakers = get_dict_field(metadata, settings.YT_FIELD_SPEAKERS)
        if speakers:
            description = f"{description}\n\nSpeakers: {speakers}"
        youtube_id = get_dict_field(metadata, settings.YT_FIELD_ID)
        self.client.videos().update(
            part="snippet",
            body={
                "id": youtube_id,
                "snippet": {
                    "title": truncate_words(
                        strip_bad_chars(resource.title), YT_MAX_LENGTH_TITLE
                    ),
                    "description": truncate_words(
                        strip_bad_chars(description), YT_MAX_LENGTH_DESCRIPTION
                    ),
                    "tags": get_dict_field(metadata, settings.YT_FIELD_TAGS),
                    "categoryId": settings.YT_CATEGORY_ID,
                },
            },
        ).execute()

        self.update_captions(resource, youtube_id)

        if privacy:
            self.update_privacy(youtube_id, privacy=privacy)

    def delete_video(self, video_id):
        """
        Delete a video from YouTube

        Args:
            video_id(str): YouTube video id

        Returns:
            int: 204 status code if successful
        """
        return self.client.videos().delete(id=video_id).execute()


def update_youtube_metadata(website: Website, version=VERSION_DRAFT):
    """ Update YouTube video metadata via the API """
    if not is_youtube_enabled() or not is_ocw_site(website):
        return
    query_id_field = get_dict_query_field("metadata", settings.YT_FIELD_ID)
    video_resources = website.websitecontent_set.filter(
        Q(metadata__resourcetype=RESOURCE_TYPE_VIDEO)
    ).exclude(Q(**{query_id_field: None}) | Q(**{query_id_field: ""}))
    if video_resources.count() == 0:
        return
    youtube = YouTubeApi()
    for video_resource in video_resources:
        youtube_id = get_dict_field(video_resource.metadata, settings.YT_FIELD_ID)
        # do not run this for any old imported videos
        if VideoFile.objects.filter(
            video__website=website, destination_id=youtube_id
        ).exists():
            try:
                youtube.update_video(
                    video_resource,
                    privacy=("public" if version == VERSION_LIVE else None),
                )
            except:  # pylint:disable=bare-except
                log.exception(
                    "Unexpected error updating metadata for video resource %d",
                    video_resource.id,
                )
