# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'سفارش شماره {}'.format(order.id)
    message = 'آقای/خانم {}\n\n سفارش شما با موفقیت ثبت گردید. شماره سفارش شما {} می‌باشد.'.format(order.last_name, order.id)
    mail_sent = send_mail(subject, message, 'info.planome@gmail.com', [order.email, 'info.planome@gmail.com'])
    return mail_sent
