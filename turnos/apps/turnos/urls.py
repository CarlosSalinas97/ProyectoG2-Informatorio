from django.contrib import admin
from django.urls import path
from . import views

app_name="turnos"

urlpatterns = [
    path('ver/<str:pk>',views.ListarTurnos, name = "listar"),
    path('solicitar/<str:pk>',views.SolicitarTurno, name='solicitar'),
    path('turnos/',views.ListarTurnosClientes, name = "listarTurnosClientes"),
]