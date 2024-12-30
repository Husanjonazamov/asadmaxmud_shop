# Generated by Django 5.1.4 on 2024-12-29 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bot", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdvertisingModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Reklama nomi")),
                (
                    "video",
                    models.FileField(
                        upload_to="ads_video/",
                        verbose_name="Reklama videosini kiriting",
                    ),
                ),
                (
                    "is_activate",
                    models.BooleanField(
                        default=True, help_text="Reklama faoligini belgilang"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Reklama",
                "verbose_name_plural": "Reklama",
                "db_table": "Advertising",
                "managed": True,
            },
        ),
    ]