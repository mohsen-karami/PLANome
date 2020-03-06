# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, SubCategory, Product, Customer
from cart.forms import CartAddProductForm
from orders.forms import OrderAuthenticateForm, OrderCreateForm
from django.contrib.auth.hashers import make_password, check_password


def home_page(request):
    food = get_object_or_404(Category, slug='food')
    drink = get_object_or_404(Category, slug='drink')
    personal_care = get_object_or_404(Category, slug='personal-care')
    home_care = get_object_or_404(Category, slug='home-care')
    return render(request, 'shop/home.html', {'food': food, 'drink': drink, 'personal_care': personal_care, 'home_care': home_care})

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
    else:
        category = subcategory.parent.all()
        category = category[0].parent.all()
        category_list = []
        for i in range(0, len(category)):
            category_list.append(category[i])
        products = Product.objects.filter(subcategory=subcategory)
    return render(request, 'shop/product/product_list.html', {'products': products, 'subcategory': subcategory, 'category_list': category_list})

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
    return render(request, 'shop/product/product_detail.html', {'product': product, 'cart_product_form': cart_product_form, 'category_list': category_list})


def user_authenticate(request):
    if request.method == 'POST':
        form = OrderAuthenticateForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.filter(phone_number=request.POST['phone_number'])
            if customer:
                if check_password(form.cleaned_data['password'], customer[0].password):
                    request.session['customer'] = customer[0]
                    request.session.save()
                    return render(request, 'shop/user/management.html', {'customer': customer[0]})
                else:
                    form = OrderAuthenticateForm()
                    return render(request, 'shop/user/authenticate.html', {'form': form})
            else:
                form = OrderCreateForm()
                return render(request, 'shop/user/register.html', {'form': form, 'phone_number': request.POST['phone_number']})
        else:
            form = OrderAuthenticateForm()
    else:
        form = OrderAuthenticateForm()
    return render(request, 'shop/user/authenticate.html', {'form': form})



def user_register(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.filter(phone_number=request.POST['phone_number'])
            if customer:
                formPassword = make_password(form.cleaned_data['password'])
                if formPassword == customer[0].password:
                    request.session['customer'] = customer[0]
                    request.session.save()
                    return render(request, 'shop/user/management.html', {'customer': customer[0]})
                else:
                    form = OrderAuthenticateForm()
                    return render(request, 'shop/user/authenticate.html', {'form': form})
            else:
                if form.cleaned_data['password'] == form.cleaned_data['rePassword']:
                    formPassword = make_password(form.cleaned_data['password'])
                    customer = form.save(commit=False)
                    customer.password = formPassword
                    customer.save()
                    request.session['customer'] = customer
                    request.session.save()
                    return render(request, 'shop/user/management.html', {'customer': customer})
                else:
                    form = OrderCreateForm(request.POST)
                    return render(request, 'shop/user/register.html', {'form': form})
        else:
            form = OrderCreateForm()
    else:
        form = OrderCreateForm()
    return render(request, 'shop/user/register.html', {'form': form})

def user_management(request):
    customer = request.session['customer']
    return render(request, 'shop/user/management.html', {'customer': customer})

def user_exit(request):
    del request.session['customer']
    return redirect('/')
