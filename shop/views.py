from django.shortcuts import render, get_object_or_404

import json


def index(req):
    """Индексная страница"""
    configs = []
    with open('../app/config/config.json', 'w') as conf:
        configs = json.load(conf)
    return render(req, 'shop/index.html', context={
        'title': 'Элитные изделия из кожи ручной работы',
        'configs': configs
    })

