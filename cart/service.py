from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from customer.models import Customer
from order.models import Order
from shop.models import Product
from cart.cart import Cart
from cart.forms import CartSubmitOrder

from core.get_config import get_config


class CartService:
    @staticmethod
    def cart_submit(req):
        form = CartSubmitOrder(req.POST)
        # if not form.is_valid():
        #     return HttpResponse(status=500)

        config = get_config()
        cart = Cart(req)

        try:
            customer = Customer.objects.get(contact_data=form.data['contact_data'])
        except ObjectDoesNotExist:
            customer = Customer.objects.create(
                contact_name=form.data['contact_name'],
                contact_type=form.data['contact_type'],
                contact_data=form.data['contact_data']
            )

        order = Order.objects.create(
            customer=customer,
            total_price=cart.get_total_price()
        )
        order.products.set(cart.get_cart_products())  # Для manyToManyField используем SET
        order.save()

        text_content = ''
        for pid, val in cart.cart.items():
            text_content += 'Товар: <a href="'+settings.MAIN_HOST + reverse("shop:product", args=[int(pid)])+'">Продукт</a> | '
            text_content += f'Количество: {val["quantity"]} | Цена за еденицу: {val["price"]} \n'
        text_content += f'Покупатель {customer.contact_name} | Способ связи: {config["contactTypeList"][customer.contact_type]}: {customer.contact_data} \n'
        text_content += f'Заказ: <a href="{settings.MAIN_HOST}/order/{order.id}">{order.id}</a>'

        html_content = render_to_string('order-mail.html', {
            'cart': cart,
            'contact_name': customer.contact_name,
            'contact_type': config["contactTypeList"][customer.contact_type],
            'contact_data': customer.contact_data,
            'product_url': settings.MAIN_HOST + '/product/',
            'order_link': f'{settings.MAIN_HOST}/order/{order.id}',
        })

        subject, from_email, to = f'Заказ на {config["companyName"]}', '', [settings.EMAIL_CORNELIUS, settings.EMAIL_ADMIN]
        email = EmailMultiAlternatives(subject, text_content, to=to)
        email.attach_alternative(html_content, "text/html")
        email.send()

        cart.clear()

        return render(req, 'order-completed.html', context={'title': 'Заказ успешно получен!'})