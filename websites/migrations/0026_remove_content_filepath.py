# Generated by Django 3.1.6 on 2021-05-12 21:29

from django.db import migrations


def unset_non_page_content_paths(apps, schema_editor):
    """
    Blanks 'dirpath' and 'filename' values for all WebsiteContent records that do not represent page content.
    The destination filepath for these types of WebsiteContent records comes from the site config, so having non-blank
    values for these fields is misleading.
    """
    WebsiteContent = apps.get_model("websites", "WebsiteContent")
    WebsiteContent.objects.filter(is_page_content=False).update(dirpath="", filename="")


class Migration(migrations.Migration):

    dependencies = [
        ("websites", "0025_update_sync_checksum"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="websitecontent",
            name="content_filepath",
        ),
        migrations.RunPython(unset_non_page_content_paths, migrations.RunPython.noop),
    ]
