
from django.contrib import admin
from django.urls import path
from menusapp import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login_view),
    path('dashboard/', views.dashboard),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'), 
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('crear_menu/', views.crear_menu, name='crear_menu'),
    path('listar_menu/', views.listar_menu, name='listar_menu'),
    path('mangas/', views.mangas),
    path('ropa/', views.ropa),
    path('figuras/', views.figuras),
    path('otros/', views.otros),
    path('politicas/', views.politicas),
]
