""" Scans the starter project directory in the local filesystem and creates/updates relevant db records """
import os
from collections import defaultdict

from django.conf import settings
from django.core.management import BaseCommand

from websites.constants import WEBSITE_CONFIG_FILENAME, STARTER_SOURCE_LOCAL
from websites.models import WebsiteStarter

LOCAL_STARTERS_DIR = "localdev/starters/"


class Command(BaseCommand):
    """ Scans the starter project directory in the local filesystem and creates/updates relevant db records """

    help = __doc__

    def add_arguments(self, parser):
        parser.add_argument(
            "-k",
            "--keep",
            dest="keep",
            action="store_true",
            help="If the start project already exists in the db, do not overwrite the config even if it has changed.",
        )

    def handle(self, *args, **options):
        local_starter_projects_path = os.path.join(
            settings.BASE_DIR, LOCAL_STARTERS_DIR
        )
        _, starter_project_dir_names, _ = next(os.walk(local_starter_projects_path))
        results = defaultdict(list)

        for dir_name in starter_project_dir_names:
            with open(
                os.path.join(
                    local_starter_projects_path, dir_name, WEBSITE_CONFIG_FILENAME
                )
            ) as f:
                config_contents = f.read().strip()
            if not config_contents:
                continue
            starter, created = WebsiteStarter.objects.get_or_create(
                path=os.path.join(LOCAL_STARTERS_DIR, dir_name),
                name=dir_name,
                source=STARTER_SOURCE_LOCAL,
                defaults=dict(config=config_contents),
            )
            updated = False
            if (
                not created
                and options["keep"] is False
                and starter.config != config_contents
            ):
                starter.config = config_contents
                starter.save()
                updated = True
            if created:
                results["created"].append(dir_name)
            if updated:
                results["updated"].append(dir_name)

        if results:
            self.stdout.write(self.style.SUCCESS(dict(results)))
        else:
            self.stdout.write(self.style.WARNING("No changes detected."))