# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Category, SubCategory, Product, Store


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'is_parent']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(SubCategory, SubCategoryAdmin)

class StoreAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Store, StoreAdmin)

class ProductAdmin(admin.ModelAdmin):
    class Media:
        css = {
             'all': ('css/admin/product.css',)
        }
    list_display = ['name', 'subcategory', 'price', 'off_price', 'stock', 'available', 'store']
    list_filter = ['available', 'created', 'updated', 'subcategory', 'store']
    search_fields = ('name',)
    list_editable = ['price', 'off_price', 'stock', 'available', 'store']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
