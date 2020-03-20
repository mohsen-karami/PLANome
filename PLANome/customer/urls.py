from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^authenticate/$', views.customer_authenticate, name='customer_authenticate'),
    url(r'^register/$', views.customer_register, name='customer_register'),
    url(r'^management/$', views.customer_management, name='customer_management'),
    url(r'^exit/$', views.customer_exit, name='customer_exit')
]
