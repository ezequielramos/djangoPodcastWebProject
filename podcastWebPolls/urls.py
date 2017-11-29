from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^front/(?P<webpage>\w+)$', views.webpage, name='webpage'),
    url(r'^list/usuarios$', views.usuarios, name='usuarios'),
    url(r'^list/usuarios/(?P<userId>\w+)$', views.usuarios, name='usuarios'),
    url(r'^list/categorias$', views.categorias, name='categorias'),
    url(r'^list/categorias/(?P<categoryId>\w+)$', views.categorias, name='categorias'),
    url(r'^list/jingles$', views.jingles, name='jingles'),
    url(r'^list/jingles/(?P<jingleId>\w+)$', views.jingles, name='jingles'),
]