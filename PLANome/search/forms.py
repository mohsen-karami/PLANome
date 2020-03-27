# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django import forms
from .models import Search


class searchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['search_unit',]
