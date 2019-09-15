from django.shortcuts import render, get_object_or_404

from shop.models import *

import json

from os import path

BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
CONFIG_PATH = path.join(BASE_DIR, 'app', 'config', 'config.json')


def index(req):
    """Индексная страница"""
    with open(CONFIG_PATH, 'r') as conf:
        configs = json.load(conf)

    slider = MainSlider.objects.all()
    reviews = Review.objects.all()
    clients = OurClients.objects.all()
    works = OurWorks.objects.all()
    top_sale = Product.objects.filter(is_top_sale=True)

    slider_range = range(slider.count())

    return render(req, 'shop/index.html', context={
        'title': 'Элитные изделия из кожи ручной работы',
        'configs': configs,
        'slider': slider,
        'slider_range': slider_range,
        'reviews': reviews,
        'clients': clients,
        'works': works,
        'top_sale': top_sale,
    })

