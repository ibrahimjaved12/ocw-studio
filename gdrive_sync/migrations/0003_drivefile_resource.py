# Generated by Django 3.1.12 on 2021-09-15 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("websites", "0034_website_title_index"),
        ("gdrive_sync", "0002_drivefile_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="drivefile",
            name="resource",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="websites.websitecontent",
            ),
        ),
    ]
