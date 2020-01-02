# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from planome.models import Customer
from django.utils.translation import ugettext_lazy as _

class OrderAuthenticateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone_number',]
        labels = {
            'phone_number': _('شماره تماس'),
        }


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'address', 'postal_code', 'phone_number']
        labels = {
            'first_name': _('نام'),
            'last_name': _('نام خانوادگی'),
            'address': _('آدرس'),
            'postal_code': _('کدپستی'),
            'phone_number': _('شماره تماس'),
        }
