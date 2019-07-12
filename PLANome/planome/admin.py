# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Category, SubCategory, Product


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
    list_display = ['name', 'slug', 'subcategory', 'price', 'stock', 'available', 'created', 'updated', 'store']
    list_filter = ['available', 'created', 'updated', 'subcategory', 'store']
    list_editable = ['price', 'stock', 'available', 'store']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)
