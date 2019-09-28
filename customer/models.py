from django.db import models
from core.get_config import get_config


def get_contact_lists():
    list_contacts = get_config()['contactTypeList']
    tuple_contact = [(k, v) for k, v in list_contacts.items()]
    return tuple_contact


class Customer(models.Model):
    """Модель покупателя."""
    contact_name = models.CharField(max_length=255, verbose_name='Имя заказчика')
    contact_type = models.CharField(max_length=12, choices=get_contact_lists(), default='tel', verbose_name='Тип связи')
    contact_data = models.CharField(max_length=255, unique=True, verbose_name='Данные для контакта')
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return f'{self.contact_name} {self.contact_type} {self.contact_data}'
