# Generated by Django 2.2.9 on 2019-12-30 11:44

from django.db import migrations
import django_resized.forms
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20191228_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourworks',
            name='img',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=72, size=[1600, 960], upload_to=shop.models.works_image_file_path, verbose_name='Фото товара'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=72, size=[1600, 960], upload_to=shop.models.product_image_file_path, verbose_name='Фото товара'),
        ),
    ]