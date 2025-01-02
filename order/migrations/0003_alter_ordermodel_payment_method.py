# Generated by Django 5.1.4 on 2025-01-01 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0002_remove_ordermodel_basket_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordermodel",
            name="payment_method",
            field=models.CharField(
                choices=[("cash", "Naqt pul")],
                default="cash",
                max_length=50,
                verbose_name="To'lov turi",
            ),
        ),
    ]