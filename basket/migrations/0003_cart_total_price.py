# Generated by Django 5.1.4 on 2024-12-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_cartitem_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Umumiy narx'),
        ),
    ]