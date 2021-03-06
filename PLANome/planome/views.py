# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Product
from cart.forms import CartAddProductForm


def home_page(request):
    food = get_object_or_404(Category, slug='food')
    drink = get_object_or_404(Category, slug='drink')
    personal_care = get_object_or_404(Category, slug='personal-care')
    home_care = get_object_or_404(Category, slug='home-care')
    categories = {food, drink, personal_care, home_care}
    return render(request, 'shop/home.html', {'categories': categories})

def subcategory_list(request, category_slug):
    categories = Category.objects.all()
    category = get_object_or_404(Category, slug=category_slug)
    subcategories = SubCategory.objects.filter(category=category, is_parent=True)
    return render(request, 'shop/subcategory_list.html', {'categories': categories, 'category': category, 'subcategories': subcategories})

def product_list(request, subcategory_slug):
    subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)

    if subcategory.is_parent:
        category = subcategory.parent.all()
        category_list = []
        for i in range(0, len(category)):
            category_list.append(category[i])
        products = Product.objects.none()
        for subcategories in subcategory.parent.all():
            products = products | Product.objects.filter(subcategory=subcategories)
        parent_subcategory = None
        category = subcategory.category
    else:
        category = subcategory.parent.all()
        parent_subcategory = category[0]
        category = category[0].parent.all()
        category_list = []
        for i in range(0, len(category)):
            category_list.append(category[i])
        products = Product.objects.filter(subcategory=subcategory)
        category = parent_subcategory.category
    return render(request, 'shop/product/product_list.html', {'products': products, 'subcategory': subcategory, 'category_list': category_list, 'subcategory_is_parent': subcategory.is_parent, 'parent_subcategory': parent_subcategory, 'category': category})

def product_detail(request, id, slug=None):
    if slug:
        product = get_object_or_404(Product, id=id, slug=slug)
    else:
        product = get_object_or_404(Product, id=id)
    subcategory = product.subcategory
    category = subcategory.parent.all()
    category = category[0].parent.all()
    category_list = []
    for i in range(0, len(category)):
        category_list.append(category[i])
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/product_detail.html', {'product': product, 'subcategory': subcategory, 'cart_product_form': cart_product_form, 'category_list': category_list})
