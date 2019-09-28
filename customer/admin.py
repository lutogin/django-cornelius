from django.contrib import admin
from customer.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['contact_name', 'contact_type', 'contact_data', 'created_date']
    list_filter = ['created_date', 'contact_data']
