# Generated by Django 5.1.4 on 2024-12-24 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_categorymodel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='product_images',
        ),
    ]
