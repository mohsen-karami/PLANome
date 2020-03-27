from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^authenticate/$', views.order_authenticate, name='order_authenticate'),
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^created/$', views.order_created, name='order_created'),
]
