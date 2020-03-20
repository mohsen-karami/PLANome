# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from customer.models import Customer
from django.utils.translation import ugettext_lazy as _

class OrderAuthenticateForm(forms.ModelForm):
    class Meta:
        model = Customer
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['phone_number', 'password']
        labels = {
            'phone_number': _('شماره تماس'),
            'password': _('گذرواژه')
        }


class OrderCreateForm(forms.ModelForm):
    rePassword = forms.CharField(widget=forms.PasswordInput(), label="تکرار گذرواژه")
    class Meta:
        model = Customer
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ['first_name', 'last_name', 'address', 'postal_code', 'phone_number', 'password']
        labels = {
            'first_name': _('نام'),
            'last_name': _('نام خانوادگی'),
            'address': _('آدرس'),
            'postal_code': _('کدپستی'),
            'phone_number': _('شماره تماس'),
            'password': _('گذرواژه')
        }
