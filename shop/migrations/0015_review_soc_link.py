# Generated by Django 2.2.7 on 2019-12-08 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20191009_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='soc_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ссылка'),
        ),
    ]
