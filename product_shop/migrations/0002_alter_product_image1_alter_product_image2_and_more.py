# Generated by Django 4.0.6 on 2022-07-26 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(max_length=255, upload_to='product_images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, max_length=255, upload_to='product_images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, max_length=255, upload_to='product_images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='productgrading',
            name='reviews',
            field=models.TextField(blank=True),
        ),
    ]
