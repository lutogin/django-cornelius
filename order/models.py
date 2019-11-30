from django.db import models
from shop.models import Product
from customer.models import Customer
import uuid


class Order(models.Model):
    """Модель заказа"""
    STATUS_CHOISE = (
        ('pending', 'В работе'),
        ('done', 'Выполнен'),
        ('cancel', 'Отменен'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Уникальный идентификатор ордера')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer', verbose_name='Покупатель')
    products = models.ManyToManyField(Product, related_name='products', verbose_name='Заказ')
    total_price = models.IntegerField(verbose_name='Предварительная сумма заказа')
    status = models.CharField(verbose_name='Статус выполнения ордера', choices=STATUS_CHOISE, default='pending', max_length=255)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    due_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.customer} - {self.total_price}р.'