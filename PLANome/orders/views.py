from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from .models import OrderItem, Order
from planome.models import Customer
from .forms import OrderCreateForm, OrderAuthenticateForm
from cart.cart import Cart


def order_authenticate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderAuthenticateForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.filter(phone_number=request.POST['phone_number'])
            if customer:
                order = Order.objects.create(customer=customer[0])
                for item in cart:
                    OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
                cart.clear()
                return render(request, 'orders/order/created.html', {'order': order, 'customer': customer[0]})
            else:
                form = OrderCreateForm()
                return render(request, 'orders/order/create.html', {'form': form, 'phone_number': request.POST['phone_number']})
        else:
            form = OrderAuthenticateForm()
    else:
        form = OrderAuthenticateForm()
    return render(request, 'orders/order/authenticate.html', {'cart': cart, 'form': form})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            customer = form.save()
            order = Order.objects.create(customer=customer)
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order, 'customer': customer})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})
