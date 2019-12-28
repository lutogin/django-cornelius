# Generated by Django 2.2.7 on 2019-12-28 12:56

from django.db import migrations, models
import django_resized.forms
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20191228_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainslider',
            name='img',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=75, size=[1920, 1080], upload_to=shop.models.slider_image_file_path, verbose_name='Слайд'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, null=True, quality=70, size=[1600, 960], upload_to=shop.models.product_image_file_path, verbose_name='Фото товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, choices=[('brown', 'Коричневый(стандартный)'), ('red', 'Красный'), ('blue', 'Синий'), ('black', 'Черный'), ('multicolor', 'Цветной')], default='b', max_length=10, verbose_name='Тип связи'),
        ),
    ]
