'''
Created on 1 nov. 2016

@author: Hugo
'''
from django.conf.urls import url
from . import views

app_name = 'biblioteca'
urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    
    url(r'^autor/$', views.AutorView, name='biblioteca/autor'),
    url(r'^autor/delete/(?P<id>\d+)/$',views.AutorDelete, name='biblioteca/autor/delete'),
    url(r'^autor/update/(?P<id>\d+)/$',views.AutorUpdate, name='biblioteca/autor/update'),
    
    url(r'^editorial/$', views.EditorialView, name='biblioteca/editorial'),
    url(r'^editorial/delete/(?P<id>\d+)/$',views.EditorialDelete, name='biblioteca/editorial/delete'),
    url(r'^editorial/update/(?P<id>\d+)/$',views.EditorialUpdate, name='biblioteca/editorial/update'),
    
    url(r'^libro/$', views.LibroView, name='biblioteca/libro'),
    url(r'^libro/listar/$', views.LibroList, name='biblioteca/libro/listar'),
    url(r'^libro/delete/(?P<id>\d+)/$',views.LibroDelete, name='biblioteca/libro/delete'),
    url(r'^libro/update/(?P<id>\d+)/$',views.LibroUpdate, name='biblioteca/libro/update'),
]
