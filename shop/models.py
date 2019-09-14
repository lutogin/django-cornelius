from django.db import models
from django.urls import reverse

from PIL import Image

import uuid
import os


def product_image_file_path(instance, filename):
    """Генерирует имя фото и возвращает путь с именем"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('static/img/products', filename)


def slider_image_file_path(instance, filename):
    """Генерирует имя фото и возвращает путь с именем для слайдера"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('static/img/slider', filename)


class Category(models.Model):
    """Модель типа товара"""
    name = models.CharField(max_length=255, verbose_name='Категория товара')
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
    """Модель для фото продукта"""
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
            return u'<img src="{0}" width="100"/>'.format(self.image.url)
        else:
            return '(Нет изображения)'
    admin_image.short_description = 'Фото торвара'
    admin_image.allow_tags = True

    def __str__(self):
        return self.admin_image()


class Product(models.Model):
    """Базовая модель продукта"""
    title = models.CharField(max_length=255, verbose_name='Титл товара')
    type = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(verbose_name='Подробное описание товара')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(verbose_name='Наличие товара', default=True)
    photo = models.ManyToManyField(Photo, verbose_name='Фото товара')

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Review(models.Model):
    """Модель отзывов"""
    fio = models.CharField(max_length=255)
    position = models.CharField(max_length=255, blank=True)
    review_text = models.TextField()


class MainSlider(models.Model):
    """Модель слайдера"""
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to=slider_image_file_path, verbose_name='Слайд')
