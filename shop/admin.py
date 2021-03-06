from django.contrib import admin
from shop.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'is_top_sale', 'created_date']
    list_filter = ['created_date']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ('admin_image',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(MainSlider)
class MainSliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'img', 'description']


@admin.register(OurClients)
class OurClientsAdmin(admin.ModelAdmin):
    list_display = ['title', 'img', 'link']


@admin.register(OurWorks)
class OurWorksAdmin(admin.ModelAdmin):
    list_display = ['product', 'img', 'large_img']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['fio', 'soc_link', 'review_text']


@admin.register(Engraving)
class EngravingAdmin(admin.ModelAdmin):
    list_display = ['img']


