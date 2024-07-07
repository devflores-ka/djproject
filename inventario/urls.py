from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingresar_inventario, name='ingresar_inventario'),
    path('success/', views.inventario_success, name='inventario_success'),
]
