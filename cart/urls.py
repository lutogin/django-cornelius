from django.urls import re_path
from cart import views

app_name = 'cart'

urlpatterns = [
    re_path(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='CartRemove'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='CartAdd'),
    re_path(r'^update/$', views.cart_update, name='CartUpdate'),
    re_path(r'^get-cart-api/$', views.get_cart_api, name='GetCartApi'),
    re_path(r'^form-check/$', views.form_check, name='CartFormCheck'),
    re_path(r'^submit/$', views.cart_submit, name='CartSubmit'),
    re_path(r'^$', views.cart_detail, name='CartDetail'),
]
