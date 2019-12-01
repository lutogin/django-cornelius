# Generated by Django 2.2.5 on 2019-09-28 14:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0011_category_names'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Уникальный идентификатор ордера', primary_key=True, serialize=False)),
                ('total_price', models.IntegerField(verbose_name='Предварительная сумма заказа')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='customer.Customer', verbose_name='Покупатель')),
                ('products', models.ManyToManyField(related_name='products', to='shop.Product', verbose_name='Заказ')),
            ],
        ),
    ]
