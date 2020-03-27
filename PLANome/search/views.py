# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import searchForm
from planome.models import Product
from django.shortcuts import render


def search_form(request):
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            search_unit = request.POST['search_unit']
            products = Product.objects.filter(name__icontains = search_unit)
            return render(request, 'searchField.html', {'form': form, 'search_unit': search_unit, 'products': products})
    else:
        form = searchForm()
    return render(request, 'searchField.html', {'form': form})
