# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from .models import Order
from django.utils.translation import ugettext_lazy as _

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'phone_number']
        labels = {
            'first_name': _('نام'),
            'last_name': _('نام خانوادگی'),
            'email': _('ایمیل'),
            'address': _('آدرس'),
            'postal_code': _('کدپستی'),
            'phone_number': _('شماره تماس'),
        }
