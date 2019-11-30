from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from shop.models import Product
from cart.cart import Cart
from cart.service import CartService

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
    """Сохранить изменения в корзине"""
    # Пример получения данных с body запроса
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
    return CartService.cart_submit(req)
