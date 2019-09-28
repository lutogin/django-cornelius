from django.urls import re_path
from cart.views import *

app_name = 'cart'

urlpatterns = [
    re_path(r'^remove/(?P<product_id>\d+)/$', cart_remove, name='CartRemove'),
    re_path(r'^add/(?P<product_id>\d+)/$', cart_add, name='CartAdd'),
    re_path(r'^update/$', cart_update, name='CartUpdate'),
    re_path(r'^get-cart-api/$', get_cart_api, name='GetCartApi'),
    re_path(r'^submit/$', cart_submit, name='CartSubmit'),
    re_path(r'^$', cart_detail, name='CartDetail'),
]
