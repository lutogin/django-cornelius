from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.urls import reverse

from cart.cart import Cart
# from cart.forms import CartAddProductForm

from shop.models import Product
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


def cart_detail(req):
    cart = Cart(req)
    return render(req, 'detail.html', context={
        'title': 'Ваша корзина товаров',
        'cart': cart
    })


@require_POST
def cart_submit(req):
    from django.core.mail import EmailMessage
    from core.get_config import get_config

    config = get_config()
    cart = Cart(req)

    body_unicode = req.body.decode('utf-8')
    body = json.loads(body_unicode)

    contact_name = body['contactName']
    contact_type = config['contactTypeList'][body['contactType']]
    contact_data = body['contactData']

    body = ''
    for pid, val in cart.cart.items():
        body += f'Товар: {reverse("shop:product", args=pid)} | количество: {val["quantity"]} | цена за еденицу: {val["price"]}'
    body += f'Покупатель {contact_name}, способ связи: {contact_type}: {contact_data}'

    email = EmailMessage('TEST', body, to=['lutogin@gmail.com'])
    email.send()
    cart.clear()

    return HttpResponse(json.dumps({'url': reverse('shop:index')}), status=200)
    # return redirect()
