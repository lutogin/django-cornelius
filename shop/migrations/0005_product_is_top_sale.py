# Generated by Django 2.2.5 on 2019-09-15 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190915_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_top_sale',
            field=models.BooleanField(default=True, verbose_name='Топ продаж'),
        ),
    ]
