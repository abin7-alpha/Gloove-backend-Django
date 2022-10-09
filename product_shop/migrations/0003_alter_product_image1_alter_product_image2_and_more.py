# Generated by Django 4.0.6 on 2022-07-26 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_shop', '0002_alter_product_image1_alter_product_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(max_length=255, upload_to='media/product_images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, max_length=255, upload_to='media/product_images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, max_length=255, upload_to='media/product_images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='productgrading',
            name='images',
            field=models.FileField(blank=True, upload_to='media/user_review_images'),
        ),
    ]