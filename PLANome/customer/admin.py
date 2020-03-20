# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'address', 'postal_code', 'phone_number', 'created', 'updated']
admin.site.register(Customer, CustomerAdmin)
