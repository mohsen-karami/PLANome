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
            'first_name': _('نام').encode('utf-8'),
            'last_name': _('نام خانوادگی').encode('utf-8'),
            'email': _('ایمیل').encode('utf-8'),
            'address': _('آدرس').encode('utf-8'),
            'postal_code': _('کدپستی').encode('utf-8'),
            'phone_number': _('شماره تماس').encode('utf-8'),
        }
