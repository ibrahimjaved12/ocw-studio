# Generated by Django 3.1.13 on 2021-11-17 21:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("websites", "0041_build_ids"),
    ]

    operations = [
        migrations.AddField(
            model_name="website",
            name="draft_last_published_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="draft_publisher",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="website",
            name="live_last_published_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="live_publisher",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
