from django.shortcuts import render
from datetime import datetime as dt
from order.models import *
from core.get_config import get_config
from django.conf import settings

config = get_config()


def order_view(req, order_id, status=None):
    """Страница заказа, для управляющего."""
    order = Order.objects.get(id=order_id)

    if status and order.status != status:
        order.due_date = dt.now()
        order.status = status
        order.save()

    return render(req, 'view.html', context={
        'order': order,
        'contact_type': config['contactTypeList'][order.customer.contact_type],
        'host': settings.MAIN_HOST
    })
