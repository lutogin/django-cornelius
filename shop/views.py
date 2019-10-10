from django.shortcuts import render, get_object_or_404
from core.get_config import get_config
from shop.models import *


def index(req):
    """Индексная страница"""
    slider = MainSlider.objects.all()
    reviews = Review.objects.all()
    clients = OurClients.objects.all()
    works = OurWorks.objects.all()
    top_sale = Product.objects.filter(is_top_sale=True)

    slider_range = range(slider.count())

    return render(req, 'index.html', context={
        'title': 'Элитные изделия из кожи ручной работы',
        'slider': slider,
        'slider_range': slider_range,
        'reviews': reviews,
        'clients': clients,
        'works': works,
        'top_sale': top_sale,
    })


def category_products(req, category_slug: str):
    """Контроллер выбор товаров по категории"""
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(slug=category_slug)

    return render(req, 'category.html', context={
        'title': category.names,
        'products': products,
        'category': category,
    })


def product_detail(req, p_id: int):
    """Контроллер страници товара"""
    product = get_object_or_404(Product, id=p_id, available=True)

    # cart_product_form = CartAddProductForm()

    return render(req, 'product.html', context={
        'title': product.title,
        'product': product,
        # 'cart_product_form': cart_product_form
    })


def engraving(req):
    engraving_obj = Product.objects.filter(type__slug='engraving')

    return render(req, 'engraving.html', context={
        'title': 'Примеры выполнения гравировок',
        'engraving': engraving_obj
    })
