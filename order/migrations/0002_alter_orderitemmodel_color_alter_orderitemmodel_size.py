# Generated by Django 5.1.4 on 2024-12-25 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemmodel',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.colormodel', verbose_name='Rang'),
        ),
        migrations.AlterField(
            model_name='orderitemmodel',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.sizemodel', verbose_name='O‘lcham'),
        ),
    ]
