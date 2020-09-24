from django.contrib import admin
from django.urls import path
from . import views

app_name="turnos"

urlpatterns = [
    path('todos/',views.ListarTurnos, name = "listar"),
    path('solicitar/<str:pk>',views.SolicitarTurno.as_view(), name='solicitar'),
    #path('horarios/',views.HorariosDisponibles.as_view(), name='horarios'),
    #path('disponibles/',views.TurnosDisponibles.as_view(), name='disponibles'),
]