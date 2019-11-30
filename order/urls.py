from django.urls import re_path
from order.views import *

app_name = 'order'

urlpatterns = [
    re_path(r'^(?P<order_id>[a-z0-9-]{36})/$', order_view, name='OrderView'),
    re_path(r'^(?P<order_id>[a-z0-9-]{36})/(?P<status>(cancel|done))/$', order_view, name='OrderChangeStatus'),
]
