# Generated by Django 3.1.12 on 2021-08-09 17:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("websites", "0034_website_title_index"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video",
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
                ("source_key", models.CharField(max_length=2048, unique=True)),
                ("status", models.CharField(default="Created", max_length=50)),
                (
                    "website",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="websites.website",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="VideoJob",
            fields=[
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "job_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("status", models.CharField(blank=True, max_length=50, null=True)),
                ("error_code", models.CharField(blank=True, max_length=24, null=True)),
                ("error_message", models.TextField(blank=True, null=True)),
                (
                    "video",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="videos.video"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="VideoFile",
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
                ("s3_key", models.CharField(max_length=2048, unique=True)),
                ("destination", models.CharField(max_length=48)),
                (
                    "destination_id",
                    models.CharField(max_length=256, null=True, blank=True),
                ),
                (
                    "video",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="videofiles",
                        to="videos.video",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
