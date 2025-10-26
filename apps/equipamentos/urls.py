from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('equipamentos/', views.lista_equipamentos, name='lista_equipamentos'),
    path('buscar/', views.buscar_equipamentos, name='buscar_equipamentos'),
]