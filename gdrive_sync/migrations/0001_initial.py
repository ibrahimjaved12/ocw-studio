# Generated by Django 3.1.12 on 2021-08-05 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("websites", "0034_website_title_index"),
    ]

    operations = [
        migrations.CreateModel(
            name="DriveApiQueryTracker",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "api_call",
                    models.CharField(
                        choices=[("files", "files"), ("changes", "changes")],
                        max_length=128,
                        unique=True,
                    ),
                ),
                ("last_page", models.CharField(blank=True, max_length=2048, null=True)),
                ("last_dt", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DriveFile",
            fields=[
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "file_id",
                    models.CharField(max_length=128, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=32767)),
                ("mime_type", models.CharField(max_length=256)),
                ("checksum", models.CharField(max_length=32)),
                ("s3_key", models.CharField(blank=True, max_length=32767, null=True)),
                ("download_link", models.URLField()),
                ("status", models.CharField(default="Created", max_length=50)),
                ("modified_time", models.DateTimeField(blank=True, null=True)),
                ("created_time", models.DateTimeField(blank=True, null=True)),
                ("drive_path", models.CharField(max_length=2048)),
                (
                    "website",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="websites.website",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
