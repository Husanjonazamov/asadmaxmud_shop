# Generated by Django 5.1.4 on 2024-12-28 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Banner nomi')),
                ('image', models.ImageField(upload_to='banner/', verbose_name='Banner Rasmi')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banner',
                'db_table': 'banner',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, verbose_name='Kategoriya nomi')),
                ('image', models.ImageField(upload_to='category/', verbose_name='Kategorya rasmi')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(choices=[("Ko'k", "Ko'k"), ('Qizil', 'Qizil'), ('Qora', 'Qora'), ('Yashil', 'Yashil'), ('Oq', 'Oq'), ('Sariq', 'Sariq'), ('Kulrang', 'Kulrang'), ('Jigarrang', 'Jigarrang'), ('Pushti', 'Pushti'), ('Siyohrang', 'Siyohrang')], max_length=55, verbose_name='nomini kiriting')),
                ('image', models.ImageField(upload_to='color/', verbose_name='Rang tasviri')),
            ],
            options={
                'verbose_name': 'Rang',
                'verbose_name_plural': 'Ranglar',
                'db_table': 'color',
            },
        ),
        migrations.CreateModel(
            name='PromotionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Aksiya nomi')),
            ],
            options={
                'verbose_name': 'Aksiyalar',
                'verbose_name_plural': 'Aksiyalar',
                'db_table': 'promotion',
            },
        ),
        migrations.CreateModel(
            name='SizeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('size_name', models.CharField(max_length=50, verbose_name='O‘lcham nomi')),
            ],
            options={
                'verbose_name': 'O‘lcham',
                'verbose_name_plural': 'O‘lchamlar',
                'db_table': 'size',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Mahsulot nomi')),
                ('description', models.TextField(verbose_name='Tavsif')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Narx')),
                ('discount_percentage', models.PositiveIntegerField(blank=True, null=True, verbose_name='Chegirma foizi')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Chegirma narxi')),
                ('main_image', models.ImageField(upload_to='products/', verbose_name='Mahsulotning Asosiy Rasmi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.categorymodel', verbose_name='Kategoriya')),
                ('color', models.ManyToManyField(related_name='products', to='product.colormodel', verbose_name='Ranglar')),
                ('promotion', models.ManyToManyField(blank=True, null=True, to='product.promotionmodel', verbose_name='Aksiyalar')),
                ('size', models.ManyToManyField(related_name='products', to='product.sizemodel', verbose_name='O‘lchamlar')),
            ],
            options={
                'verbose_name': 'Mahsulot',
                'verbose_name_plural': 'Mahsulotlar',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='product_image/', verbose_name='Mahsulot Rasmi')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productmodel', verbose_name='Mahsulot')),
            ],
            options={
                'verbose_name': 'Mahsulot Rasmi',
                'verbose_name_plural': 'Mahsulot Rasmi',
                'db_table': 'product_image',
            },
        ),
    ]
