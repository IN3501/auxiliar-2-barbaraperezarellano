from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
	path('pestaña/', views.pestaña, name='pestaña'),
	path('equipodocente/', views.equipodocente, name='equipodocente'),
	path('seleccion/', views.seleccion, name='seleccion')
]