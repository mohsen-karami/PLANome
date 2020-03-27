from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from .models import OrderItem, Order
from customer.models import Customer
from .forms import OrderCreateForm, OrderAuthenticateForm
from django.contrib.auth.hashers import make_password, check_password
from cart.cart import Cart


def order_authenticate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderAuthenticateForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.filter(phone_number=request.POST['phone_number'])
            if customer:
                if check_password(form.cleaned_data['password'], customer[0].password):
                    request.session['customer'] = customer[0]
                    request.session.save()
                    return render(request, 'orders/order/cart_review.html', {'cart': cart, 'customer': customer[0]})
                else:
                    form = OrderAuthenticateForm()
                    return render(request, 'orders/order/authenticate.html', {'cart': cart, 'form': form})
            else:
                form = OrderCreateForm()
                return render(request, 'orders/order/create.html', {'form': form, 'phone_number': request.POST['phone_number']})
        else:
            form = OrderAuthenticateForm()
    else:
        if 'customer' in request.session:
            customer = request.session['customer']
            return render(request, 'orders/order/cart_review.html', {'cart': cart, 'customer': customer})
        else:
            form = OrderAuthenticateForm()
    return render(request, 'orders/order/authenticate.html', {'cart': cart, 'form': form})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.filter(phone_number=request.POST['phone_number'])
            if customer:
                formPassword = make_password(form.cleaned_data['password'])
                if formPassword == customer[0].password:
                    request.session['customer'] = customer[0]
                    request.session.save()
                    return render(request, 'orders/order/cart_review.html', {'cart': cart, 'customer': customer})
                else:
                    form = OrderAuthenticateForm()
                    return render(request, 'orders/order/authenticate.html', {'form': form})
            else:
                if form.cleaned_data['password'] == form.cleaned_data['rePassword']:
                    formPassword = make_password(form.cleaned_data['password'])
                    customer = form.save(commit=False)
                    customer.password = formPassword
                    customer.save()
                    request.session['customer'] = customer
                    request.session.save()
                    return render(request, 'orders/order/cart_review.html', {'cart': cart, 'customer': customer})
                else:
                    form = OrderCreateForm(request.POST)
                    return render(request, 'orders/order/create.html', {'form': form})
        else:
            form = OrderCreateForm()
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})

def order_created(request):
    cart = Cart(request)
    customer = request.session['customer']
    order = Order.objects.create(customer=customer)
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
    cart.clear()
    return render(request, 'orders/order/created.html', {'order': order, 'customer': customer})
