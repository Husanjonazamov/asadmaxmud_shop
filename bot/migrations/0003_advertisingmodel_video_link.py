# Generated by Django 5.1.4 on 2024-12-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bot", "0002_advertisingmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="advertisingmodel",
            name="video_link",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Video Linki"
            ),
        ),
    ]