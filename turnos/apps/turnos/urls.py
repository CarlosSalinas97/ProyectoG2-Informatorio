from django.contrib import admin
from django.urls import path
from . import views

app_name="turnos"

urlpatterns = [
    path('ver/<str:pk>',views.ListarTurnos, name = "listar"),
    path('solicitar/<str:pk>',views.SolicitarTurno, name='solicitar'),
    #path('horarios/<str:pk>',views.HorariosDisponibles.as_view(), name='horarios'),
    #path('disponibles/<str:pk>',views.TurnosDisponibles.as_view(), name='disponibles'),
]