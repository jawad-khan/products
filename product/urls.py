from django.conf.urls import url
from rest_framework_expiring_authtoken import views as rest_views

from . import views

urlpatterns = [
    #
    # url(r'login/$','django.contrib.auth.views.login', csrf_exempt(login),{'template_name':'products/login.html'}),
    # url(r'logout/$','django.contrib.auth.views.logout',{'next_page': '/app/login'}),
    # url(r'^home/$', views.home, name='home'),
    url(r'^address/$', views.user_address, name='address'),
    url(r'^$', views.profile, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^products/$', views.products, name='products'),
    url(r'^add_product/$', views.add_product, ),
    url(r'^delete_product/(?P<id>.+)/$', views.delete_product, name="delete_product"),
    url(r'^edit_product/(?P<id>.+)/$', views.edit_product, name="Edit_product"),
    url(r'^my_products/$', views.user_products, name='user_product'),
    url(r'^profile/$', views.profile),
    url(r'^upload_image/', views.upload_image),
    url(r'^login/', rest_views.obtain_expiring_auth_token),
    url(r'^logout/', views.logout),
    url(r'^upload_cover/', views.upload_cover),
    url(r'^change_product_image/', views.product_image),
]