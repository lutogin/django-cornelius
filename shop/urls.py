from django.urls import path, re_path
from shop.views import *

app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^engraving/?$', engraving, name='engraving'),
    re_path(r'^category/(?P<category_slug>[a-z]{3,20})', category_products, name='category'),
    re_path(r'^product/(?P<p_id>[0-9]{1,4})', product_detail, name='product'),
]
