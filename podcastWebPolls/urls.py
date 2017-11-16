from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^list/$', views.index, name='list'),
    url(r'^list/usuarios$', views.usuarios, name='usuarios'),
]