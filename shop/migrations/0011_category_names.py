# Generated by Django 2.2.5 on 2019-09-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20190915_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='names',
            field=models.CharField(default='Test', max_length=255, verbose_name='Категория товара в множ.'),
        ),
    ]
