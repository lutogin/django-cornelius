from django.contrib import admin

from shop.models import Photo, Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'available']
    list_filter = ['title', 'available']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('admin_image',)


admin.site.register(Category)
