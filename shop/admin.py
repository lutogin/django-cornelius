from django.contrib import admin

from shop.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'available']
    list_filter = ['title', 'available']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('admin_image',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


admin.site.register(MainSlider)
admin.site.register(Review)
admin.site.register(OurClients)
admin.site.register(OurWorks)
