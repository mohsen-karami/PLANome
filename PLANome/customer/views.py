# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.hashers import make_password, check_password
from orders.forms import OrderAuthenticateForm, OrderCreateForm
from django.shortcuts import render, redirect
from .models import Customer

def customer_authenticate(request):
    if request.method == 'POST':
        form = OrderAuthenticateForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.filter(phone_number=request.POST['phone_number'])
            if customer:
                if check_password(form.cleaned_data['password'], customer[0].password):
                    request.session['customer'] = customer[0]
                    request.session.save()
                    return render(request, 'customer/management.html', {'customer': customer[0]})
                else:
                    form = OrderAuthenticateForm()
                    return render(request, 'customer/authenticate.html', {'form': form})
            else:
                form = OrderCreateForm()
                return render(request, 'customer/register.html', {'form': form, 'phone_number': request.POST['phone_number']})
        else:
            form = OrderAuthenticateForm()
    else:
        form = OrderAuthenticateForm()
    return render(request, 'customer/authenticate.html', {'form': form})



def customer_register(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.filter(phone_number=request.POST['phone_number'])
            if customer:
                formPassword = make_password(form.cleaned_data['password'])
                if formPassword == customer[0].password:
                    request.session['customer'] = customer[0]
                    request.session.save()
                    return render(request, 'customer/management.html', {'customer': customer[0]})
                else:
                    form = OrderAuthenticateForm()
                    return render(request, 'customer/authenticate.html', {'form': form})
            else:
                if form.cleaned_data['password'] == form.cleaned_data['rePassword']:
                    formPassword = make_password(form.cleaned_data['password'])
                    customer = form.save(commit=False)
                    customer.password = formPassword
                    customer.save()
                    request.session['customer'] = customer
                    request.session.save()
                    return render(request, 'customer/management.html', {'customer': customer})
                else:
                    form = OrderCreateForm(request.POST)
                    return render(request, 'customer/register.html', {'form': form})
        else:
            form = OrderCreateForm()
    else:
        form = OrderCreateForm()
    return render(request, 'customer/register.html', {'form': form})

def customer_management(request):
    customer = request.session['customer']
    return render(request, 'customer/management.html', {'customer': customer})

def customer_exit(request):
    del request.session['customer']
    return redirect('/')
