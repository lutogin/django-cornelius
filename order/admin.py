from django.contrib import admin
from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'total_price', 'status', 'created_date', 'due_date']
    list_filter = ['created_date', 'customer']
