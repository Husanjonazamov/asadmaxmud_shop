# Generated by Django 5.1.4 on 2025-01-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="promotionmodel",
            name="color_code",
        ),
        migrations.AddField(
            model_name="promotionmodel",
            name="image",
            field=models.ImageField(
                default=1, upload_to="promotion_image/", verbose_name="Rasmni kiriting"
            ),
            preserve_default=False,
        ),
    ]