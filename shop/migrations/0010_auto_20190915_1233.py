# Generated by Django 2.2.5 on 2019-09-15 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20190915_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainslider',
            old_name='image',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='ourclients',
            old_name='image',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='ourworks',
            old_name='photo',
            new_name='img',
        ),
    ]
