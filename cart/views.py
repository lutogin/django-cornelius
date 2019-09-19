from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from cart.cart import Cart
# from cart.forms import CartAddProductForm

from shop.models import Product
from core.get_config import get_config


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    # form = CartAddProductForm(request.POST)
    #
    # if form.is_valid():
    #     cd = form.cleaned_data
    #     cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    cart.add(product, 1, True)

    # return redirect('cart:cart_detail')
    return HttpResponse(status=200)


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)

    # return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'detail.html', context={
        'title': 'Ваша корзина товаров',
        'cart': cart,
        'configs': get_config()
    })
