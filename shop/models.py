from django.db import models
from django.urls import reverse

from PIL import Image

import uuid
import os


def product_image_file_path(instance, filename):
    """Генерирует имя фото и возвращает путь с именем."""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('/img/products/', filename)


def slider_image_file_path(instance, filename):
    """Генерирует имя фото и возвращает путь с именем для слайдера."""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('/img/slider/', filename)


def our_clients_image_file_path(instance, filename):
    """Генерирует имя фото и возвращает путь с именем для слайдера."""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('/img/clients/', filename)


def works_image_file_path(instance, filename):
    """Генерирует имя фото и возвращает путь с именем для слайдера."""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('/img/works/', filename)


class Category(models.Model):
    """Модель типа товара."""
    name = models.CharField(max_length=255, verbose_name='Категория товара')
    names = models.CharField(max_length=255, verbose_name='Категория товара в множ.', default='Test')
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])


class Photo(models.Model):
    """Модель для фото продукта."""
    image = models.ImageField(null=True, upload_to=product_image_file_path, verbose_name='Фото товара')

    def save(self):
        super().save()  # saving image first

        img = Image.open(self.image.path)  # Open image using self

        if img.height > 1920 or img.width > 1080:
            new_img = (1920, 1080)
            img.thumbnail(new_img)
            img.save(self.image.path)  # saving image at the same path

    # Вывод картинок в админке!
    def admin_image(self):
        if self.image:
            from django.utils.html import mark_safe
            return mark_safe('<img src="{url}" width="100" height="100" />'.format(url=self.image.url))
        else:
            return '(Нет изображения)'
    admin_image.short_description = 'Фото торвара'
    admin_image.allow_tags = True

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товаров'

    def __str__(self):
        return self.image.url


class Product(models.Model):
    """Базовая модель продукта."""
    title = models.CharField(max_length=255, verbose_name='Титл товара')
    type = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(verbose_name='Подробное описание товара')
    price = models.IntegerField(verbose_name='Цена')
    available = models.BooleanField(verbose_name='Наличие товара', default=True)
    is_top_sale = models.BooleanField(verbose_name='Топ продаж', default=True)
    imgs = models.ManyToManyField(Photo, verbose_name='Фото товара', related_name='imgs')
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])

    class Meta:
        ordering = ['title', '-created_date']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title} - id{self.id}'


class MainSlider(models.Model):
    """Модель слайдера."""
    title = models.CharField(max_length=255, verbose_name='Заголовок слайда')
    description = models.CharField(max_length=255, verbose_name='Описание слайда')
    img = models.ImageField(null=True, upload_to=slider_image_file_path, verbose_name='Слайд')

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class Review(models.Model):
    """Модель отзывов."""
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=255, blank=True, verbose_name='Должность')
    review_text = models.TextField(verbose_name='Отзыв')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class OurClients(models.Model):
    """Модель Наши Клиенты."""
    title = models.CharField(max_length=255, verbose_name='Название клиента')
    img = models.ImageField(upload_to=our_clients_image_file_path, verbose_name='Иконка компании')
    link = models.CharField(max_length=255, verbose_name='Ссылка на клиента')

    class Meta:
        verbose_name = 'Наш клиент'
        verbose_name_plural = 'Нашы клиенты'


class OurWorks(models.Model):
    """Модель наших работ"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Реальный прототиа товра')
    img = models.ImageField(upload_to=works_image_file_path, verbose_name='Фото работы')
    large_img = models.BooleanField(verbose_name='Большая плитка', default=False)

    class Meta:
        verbose_name = 'Наша работа'
        verbose_name_plural = 'Нашы работы'

