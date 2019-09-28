from django.db import models
from shop.models import Product
from customer.models import Customer


class Order(models.Model):
    """Модель заказа"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer', verbose_name='Покупатель')
    products = models.ManyToManyField(Product, related_name='products', verbose_name='Заказ')
    total_price = models.IntegerField(verbose_name='Предварительная сумма заказа')
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.customer} - {self.total_price}р.'
