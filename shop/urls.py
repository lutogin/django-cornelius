from django.urls import path, re_path

from shop.views import index, category_products, product_detail

urlpatterns = [
    path('', index),
    re_path(r'^category/(?P<category_slug>[a-z]{4,20})', category_products),
    re_path(r'^product/(?P<p_id>[0-9]{1,4})', product_detail)
]
