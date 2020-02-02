from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^product/dna-(?P<id>\d+)/$', views.product_detail, name='product_detail'),
    url(r'^sub-category/(?P<subcategory_slug>[-\w]+)/$', views.product_list, name='product_list_by_subcategory'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.subcategory_list, name='subcategory_list_by_category'),
    url(r'^product/dna-(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^user/authenticate/$', views.user_authenticate, name='user_authenticate'),
    url(r'^user/register/$', views.user_register, name='user_register'),
    url(r'^user/management/$', views.user_management, name='user_management'),
    url(r'^user/exit/$', views.user_exit, name='user_exit')
]
