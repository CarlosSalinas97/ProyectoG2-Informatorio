from django.contrib import admin
from django.urls import path
from . import views

app_name = 'empresa'

urlpatterns = [
    path('registrar/',views.RegistrarEmpresa, name = "registrar"),
    path('listar/',views.Filtros, name = "listar"),
    path('listarDuenio/',views.FiltrosDuenio, name = "listarDuenio"),
    path('modificar/<str:pk>',views.Modificar.as_view(), name = "modificar"),
    path('eliminar/<str:pk>',views.Eliminar.as_view(), name = "eliminar"),
    path('turnos/',views.ListarTurnos, name = "listarTurnos"),


]