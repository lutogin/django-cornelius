from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.urls import reverse
from django.core.mail import EmailMessage

from cart.cart import Cart
from shop.models import Product
from cart.forms import CartSubmitOrder
from core.get_config import get_config

import json


@require_POST
def cart_add(req, product_id):
    cart = Cart(req)
    product = get_object_or_404(Product, id=product_id)

    cart.add(product, 1)

    # return redirect('cart:cart_detail')
    return HttpResponse(json.dumps({'counter': cart.get_counter_purchases()}), status=200)


@require_POST
def cart_remove(req, product_id):
    cart = Cart(req)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    # return redirect('cart:cart_detail')
    return HttpResponse(json.dumps({'counter': cart.get_counter_purchases()}), status=200)


@require_POST
def cart_update(req):
    body_unicode = req.body.decode('utf-8')
    body = json.loads(body_unicode)
    cart = Cart(req)

    for pid in cart.get_cart_pid():
        post_data = body[str(pid)]
        cart.update(pid, int(post_data['quantity']), post_data['engraving'])

    return HttpResponse(status=200)


def cart_detail(req):
    from cart.forms import CartSubmitOrder

    cart = Cart(req)
    return render(req, 'detail.html', context={
        'title': 'Ваша корзина товаров',
        'cart': cart,
        'submit_order_form': CartSubmitOrder
    })


@require_POST
def get_cart_api(req):
    cart = Cart(req)
    return HttpResponse(json.dumps({'cart': cart.cart}), status=200)


@require_POST
def cart_submit(req):
    """Сабмит заказа"""

    form = CartSubmitOrder(req.POST)
    if not form.is_valid():
        return HttpResponse(status=500)

    config = get_config()
    cart = Cart(req)

    # body_unicode = req.body.decode('utf-8')
    # body = json.loads(body_unicode)
    #
    # contact_name = body['contact_name']
    # contact_type = config['contactTypeList'][body['contact_type']]
    # contact_data = body['contact_data']

    contact_name = form.cleaned_data['contact_name']
    contact_type = form.cleaned_data['contact_type']
    contact_data = form.cleaned_data['contact_data']

    body = ''
    for pid, val in cart.cart.items():
        body += f'Товар: {reverse("shop:product", args=pid)} | количество: {val["quantity"]} | цена за еденицу: {val["price"]}'
    body += f'Покупатель {contact_name}, способ связи: {contact_type}: {contact_data}'

    email = EmailMessage(f'Заказ на {config["companyName"]}', body, to=['lutogin@gmail.com'])
    email.send()
    cart.clear()

    return render(req, 'order-completed.html', context={'title': 'Заказ успешно получен!'})


@require_POST
def form_check(req):
    """Проверка правильности заполнения формы"""
    body_unicode = req.body.decode('utf-8')
    body = json.loads(body_unicode)
    data = {
        'contact_name': body['contact_name'],
        'contact_type': body['contact_type'],
        'contact_data': body['contact_data']
    }


