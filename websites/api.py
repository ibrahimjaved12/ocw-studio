"""API functionality for websites"""
from typing import Optional
from uuid import UUID

from django.db.models import Q, QuerySet
from mitol.common.utils import max_or_none

from websites.constants import CONTENT_FILENAME_MAX_LEN
from websites.models import Website, WebsiteContent, WebsiteStarter


def get_valid_new_filename(
    website_pk: str, dirpath: Optional[str], filename_base: str
) -> str:
    """
    Given a filename to act as a base/prefix, returns a filename that will satisfy unique constraints,
    adding/incrementing a numerical suffix as necessary.

    Examples:
        In database: WebsiteContent(filename="my-filename")...
            get_valid_new_filename("my-filename") == "my-filename-2"
        In database: WebsiteContent(filename="my-filename-99")...
            get_valid_new_filename("my-filename-99") == "my-filename-100"
    """
    website_content_qset = WebsiteContent.objects.all_with_deleted().filter(
        website_id=website_pk, dirpath=dirpath
    )
    filename_exists = website_content_qset.filter(filename=filename_base).exists()
    if not filename_exists:
        return filename_base
    return find_available_name(
        website_content_qset,
        filename_base,
        "filename",
        max_length=CONTENT_FILENAME_MAX_LEN,
    )


def get_valid_new_slug(slug_base: str, path: str) -> str:
    """
    Given a slug to act as a base/prefix, returns a slug that will satisfy unique constraints,
    adding/incrementing a numerical suffix as necessary.
    """
    starter_qset = WebsiteStarter.objects.exclude(path=path)
    slug_exists = starter_qset.filter(slug=slug_base).exists()
    if not slug_exists:
        return slug_base
    return find_available_name(starter_qset, slug_base, "slug", max_length=30)


def find_available_name(
    website_content_qset: QuerySet,
    initial_filename_base: str,
    fieldname: str,
    max_length: Optional[int] = CONTENT_FILENAME_MAX_LEN,
) -> str:
    """
    Returns a filename with the lowest possible suffix given some base filename. If the applied suffix
    makes the filename longer than the filename max length, characters are removed from the
    right of the filename to make room.

    EXAMPLES:
    initial_filename_base = "myfile"
        Existing filenames = "myfile"
        Return value = "myfile1"
    initial_filename_base = "myfile"
        Existing filenames = "myfile", "myfile1" through "myfile5"
        Return value = "myfile6"
    initial_filename_base = "abcdefghijklmnopqrstuvwxyz" (26 characters, assuming 26 character max)
        Existing filenames = "abcdefghijklmnopqrstuvwxyz"
        Return value = "abcdefghijklmnopqrstuvwxy1"
    initial_filename_base = "abcdefghijklmnopqrstuvwxy" (25 characters long, assuming 26 character max)
        Existing filenames = "abc...y", "abc...y1" through "abc...y9"
        Return value = "abcdefghijklmnopqrstuvwx10"
    """
    # Keeps track of the number of characters that must be cut from the filename to be less than
    # the filename max length when the suffix is applied.
    chars_to_truncate = 0 if len(initial_filename_base) < max_length else 1
    # Any query for suffixed filenames could come up empty. The minimum suffix will be added to
    # the filename in that case.
    current_min_suffix = 2
    while chars_to_truncate < len(initial_filename_base):
        name_base = initial_filename_base[
            0 : len(initial_filename_base) - chars_to_truncate
        ]
        kwargs = {
            f"{fieldname}__regex": r"{name_base}[0-9]+".format(name_base=name_base)
        }
        # Find names that match the namebase and have a numerical suffix, then find the max suffix
        existing_names = website_content_qset.filter(**kwargs).values_list(
            fieldname, flat=True
        )
        max_suffix = max_or_none(
            int(filename[len(name_base) :]) for filename in existing_names
        )
        if max_suffix is None:
            return "".join([name_base, str(current_min_suffix)])
        else:
            next_suffix = max_suffix + 1
            candidate_name = "".join([name_base, str(next_suffix)])
            # If the next suffix adds a digit and causes the filename to exceed the character limit,
            # keep searching.
            if len(candidate_name) <= max_length:
                return candidate_name
        # At this point, we know there are no suffixes left to add to this filename base that was tried,
        # so we will need to remove characters from the end of that filename base to make room for a longer
        # suffix.
        chars_to_truncate = chars_to_truncate + 1
        available_suffix_digits = max_length - (
            len(initial_filename_base) - chars_to_truncate
        )
        # If there is space for 4 digits for the suffix, the minimum value it could be is 1000, or 10^3
        current_min_suffix = 10 ** (available_suffix_digits - 1)


def fetch_website(filter_value: str) -> Website:
    """
    Attempts to fetch a Website based on several properties
    """
    if len(filter_value) in {32, 36}:
        try:
            parsed_uuid = UUID(filter_value, version=4)
            website = Website.objects.filter(uuid=parsed_uuid).first()
            if website is not None:
                return website
        except ValueError:
            pass
    website_results = Website.objects.filter(
        Q(name__iexact=filter_value) | Q(title__iexact=filter_value)
    ).all()
    if len(website_results) == 0:
        raise Website.DoesNotExist(
            f"Could not find a Website with a matching uuid, name, or title ('{filter_value}')"
        )
    if len(website_results) == 1:
        return website_results[0]

    sorted_results = sorted(
        website_results, key=lambda _website: 1 if _website.name == filter_value else 2
    )
    return next(sorted_results)