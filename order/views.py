from django.shortcuts import render
from order.models import *


def order_view(req, order_id):
    """Страница заказа, для управляющего."""
    order = Order.objects.get(id=order_id)

    return render(req, 'view.html', context={
        'order': order,
    })
