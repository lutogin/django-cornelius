from django.shortcuts import render
from django.conf import settings
from datetime import datetime as dt
from django.core.mail import EmailMessage

from order.models import *
from core.get_config import get_config

config = get_config()


def order_view(req, order_id, status=None):
    """Страница заказа, для управляющего."""
    order = Order.objects.get(id=order_id)

    if status and order.status != status:
        order.due_date = dt.now()
        order.status = status
        order.save()

        text_content = f'Заказ {settings.MAIN_HOST}/order/{order.id} --> {order.status}'

        subject, from_email, to = f'Заказ на {config["companyName"]} изменен на {order.status}', settings.EMAIL_HOST_USER, [settings.EMAIL_ADMIN]
        email = EmailMessage(subject, text_content, from_email, to)
        email.send()

    return render(req, 'view.html', context={
        'order': order,
        'contact_type': config['contactTypeList'][order.customer.contact_type],
        'host': settings.MAIN_HOST
    })
