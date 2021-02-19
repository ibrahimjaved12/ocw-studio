# Generated by Django 3.1 on 2021-02-04 18:03
import json

import yaml
from django.db import migrations, models


def set_config_to_json(apps, schema_editor):
    WebsiteStarter = apps.get_model("websites", "WebsiteStarter")
    for starter in WebsiteStarter.objects.all():
        parsed_config = yaml.load(starter.config, Loader=yaml.Loader)
        starter.config = json.dumps(parsed_config)
        starter.save()


def set_config_to_yaml(apps, schema_editor):
    WebsiteStarter = apps.get_model("websites", "WebsiteStarter")
    for starter in WebsiteStarter.objects.all():
        parsed_config = json.loads(starter.config)
        starter.config = yaml.dump(parsed_config)
        starter.save()


class Migration(migrations.Migration):

    dependencies = [
        ("websites", "0005_website_fields_update"),
    ]

    operations = [
        migrations.AlterField(
            model_name="websitestarter",
            name="config",
            field=models.TextField(help_text="YML-formatted site config."),
        ),
        migrations.RunPython(set_config_to_json, set_config_to_yaml),
        migrations.AlterField(
            model_name="websitestarter",
            name="config",
            field=models.JSONField(
                help_text="Site config describing content types, widgets, etc."
            ),
        ),
    ]