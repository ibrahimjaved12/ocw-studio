# Generated by Django 3.1 on 2021-01-28 16:27
from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Group
from django.db import migrations

from websites import constants
from websites.permissions import create_global_groups


def add_global_groups(apps, schema_editor):
    """
    Create the global groups
    """
    app_config = apps.get_app_config("websites")
    app_config.models_module = True
    create_permissions(app_config, verbosity=0)
    app_config.models_module = None
    create_global_groups()


def remove_global_groups(apps, schema_editor):
    """
    Remove all global and website-specific groups
    """
    Group.objects.filter(name=constants.GLOBAL_ADMIN).delete()
    Group.objects.filter(name=constants.GLOBAL_AUTHOR).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("websites", "0007_website_owners"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="website",
            options={
                "permissions": (
                    ("publish_website", "Publish or unpublish a website"),
                    ("preview_website", "Create preview markdowm"),
                    (
                        "add_collaborators_website",
                        "Add or remove collaborators (admins, editors, etc)",
                    ),
                    ("edit_content_website", "Edit website content"),
                )
            },
        ),
        migrations.RunPython(add_global_groups, remove_global_groups),
    ]