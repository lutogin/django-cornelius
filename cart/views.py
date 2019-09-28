from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.urls import reverse
from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from core.get_config import get_config

from shop.models import Product
from customer.models import Customer
from order.models import Order
from cart.cart import Cart
from cart.forms import CartSubmitOrder

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
    form = CartSubmitOrder(req.POST)
    if not form.is_valid():
        return HttpResponse(status=500)

    config = get_config()
    cart = Cart(req)

    customer = Customer.objects.get_or_create(
        contact_name=form.cleaned_data['contact_name'],
        contact_type=form.cleaned_data['contact_type'],
        contact_data=form.cleaned_data['contact_data']
    )
    customer = customer[0] # При get_or_create вернет tuple (obj, bool)

    order = Order.objects.create(
        customer=customer,
        total_price=cart.get_total_price()
    )
    order.products.set(cart.get_cart_products()) # Для manyToManyField используем SET
    order.save()

    text_content = ''
    for pid, val in cart.cart.items():
        text_content += f'Товар: {reverse("shop:product", args=pid)} | Количество: {val["quantity"]} | Цена за еденицу: {val["price"]} \n'
    text_content += f'Покупатель {customer.contact_name} | Cпособ связи: {config["contactTypeList"][customer.contact_type]}: {customer.contact_data}'

    html_content = render_to_string('order-mail.html', {
        'cart': cart,
        'contact_name': customer.contact_name,
        'contact_type': config["contactTypeList"][customer.contact_type],
        'contact_data': customer.contact_data,
        'host': get_config()['host']
    })

    subject, from_email, to = f'Заказ на {config["companyName"]}', '', 'lutogin@gmail.com'
    email = EmailMultiAlternatives(subject, text_content, to=[to])
    email.attach_alternative(html_content, "text/html")
    email.send()

    cart.clear()

    return render(req, 'order-completed.html', context={'title': 'Заказ успешно получен!'})
