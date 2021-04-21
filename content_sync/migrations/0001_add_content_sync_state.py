# Generated by Django 3.1.6 on 2021-04-14 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("websites", "0017_rename_filepath"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContentSyncState",
            fields=[
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("current_checksum", models.CharField(max_length=64)),
                ("synced_checksum", models.CharField(max_length=64, null=True)),
                ("data", models.JSONField(null=True)),
                (
                    "content",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="content_sync_state",
                        to="websites.websitecontent",
                    ),
                ),
            ],
        ),
    ]