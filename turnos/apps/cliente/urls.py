from django.contrib import admin
from django.urls import path
from . import views

app_name = 'cliente'
urlpatterns = [
    path('RegistrarCliente/',views.RegistroCliente.as_view(), name = "registrar_cliente"),

]