# import PIL
from django.db import models
from django.urls import reverse
# from PIL import Image
from django_resized import ResizedImageField

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


import uuid
import os


def product_image_file_path(instance, filename):
    """Генерирует имя фото и возвращает путь с именем."""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('img/products/', filename)


def slider_image_file_path(instance, filename):
    """Генерирует имя фото и возвращает путь с именем для слайдера."""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('img/slider/', filename)


def our_clients_image_file_path(instance, filename):
    """Генерирует имя фото и возвращает путь с именем для слайдера."""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('img/clients/', filename)


def works_image_file_path(instance, filename):
    """Генерирует имя фото и возвращает путь с именем для слайдера."""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('img/works/', filename)


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
    image = ResizedImageField(null=True, upload_to=product_image_file_path, verbose_name='Фото товара', crop=['middle', 'center'])
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.image.path)
    #
    #     # if img.height > 1920 or img.width > 1080:
    #     base_width = img.width
    #     ratio = (base_width / float(img.size[0]))
    #     height = int((float(img.size[1]) * float(ratio)))
    #
    #     img.resize((base_width, height), PIL.Image.ANTIALIAS)
    #     super(Photo, self).save()

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

    COLOR_CHOISE = (
        ('brown', 'Коричневый(стандартный)'),
        ('red', 'Красный'),
        ('blue', 'Синий'),
        ('black', 'Черный'),
        ('multicolor', 'Цветной'),
    )  # Структура для передачи в choices

    SLUG_CHOISE = (
        ('accessory', 'Аксессуар'),
        ('bag', 'Сумка'),
        ('belt', 'Ремень'),
        ('cover', 'Обложка'),
        ('housekeeper', 'Ключница'),
        ('portmone', 'Портмоне'),
        ('purse', 'Кошелек'),
    )

    title = models.CharField(max_length=255, verbose_name='Титл товара')
    type = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=200, choices=SLUG_CHOISE, db_index=True)
    description = models.TextField(verbose_name='Подробное описание товара')
    color = models.CharField(max_length=10, choices=COLOR_CHOISE, default='b', verbose_name='Тип связи', blank=True)
    price = models.IntegerField(verbose_name='Цена')
    available = models.BooleanField(verbose_name='Наличие товара', default=True)
    is_top_sale = models.BooleanField(verbose_name='Топ продаж', default=True)
    imgs = models.ManyToManyField(Photo, verbose_name='Фото товара', related_name='imgs')
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.title} - id{self.id}'


class Engraving(models.Model):
    """Модель гравровки."""
    # title = models.CharField(max_length=255, verbose_name='Титл гравировки', blank=True)
    # price = models.IntegerField(verbose_name='Цена')
    # available = models.BooleanField(verbose_name='Наличие товара', default=True)
    img = models.OneToOneField(Photo, verbose_name='Фото товара', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Гравировка'
        verbose_name_plural = 'Гравировки'

    def __str__(self):
        return f'{self.img}'


class MainSlider(models.Model):
    """Модель слайдера."""
    title = models.CharField(max_length=255, verbose_name='Заголовок слайда')
    description = models.CharField(max_length=255, verbose_name='Описание слайда')
    # img = models.ImageField(null=True, upload_to=slider_image_file_path, verbose_name='Слайд')
    img = ResizedImageField(size=[1920, 1080], quality=75, upload_to=slider_image_file_path, verbose_name='Слайд', crop=['middle', 'center'])

    # def save(self):
    #     super().save()
    #     img = Image.open(self.img.path)
    #     file, ext = os.path.splitext(self.img.path)
    #
    #     if img.height > 2560 or img.width > 1440:
    #         img.resize((1920, 1080))
    #         img.save(self.img.path)
    #
    #     img.convert("RGB")
    #     img.save(f'{file}.webp', "WEBP")

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class Review(models.Model):
    """Модель отзывов."""
    fio = models.CharField(max_length=255, verbose_name='ФИО')
    soc_link = models.CharField(max_length=255, blank=True, verbose_name='Ссылка')
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

    def __str__(self):
        return self.title


class OurWorks(models.Model):
    """Модель наших работ"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Реальный прототиа товра')
    img = ResizedImageField(size=[800, 480], upload_to=works_image_file_path, verbose_name='Фото товара', crop=['middle', 'center'])
    large_img = models.BooleanField(verbose_name='Большая плитка', default=False)

    class Meta:
        verbose_name = 'Наша работа'
        verbose_name_plural = 'Нашы работы'

    def __str__(self):
        return self.product.title


@receiver(pre_delete, sender=Photo)
def image_model_delete(sender, instance, **kwargs):
    if instance.image.name:
        instance.image.delete(False)