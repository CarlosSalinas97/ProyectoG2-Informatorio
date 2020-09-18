
from django.contrib import admin
from django.urls import path
from . import views



app_name = 'autoevaluacion'

urlpatterns = [
    path('Listar/', views.Listar.as_view(), name = 'listar'),
    path('Auto/', views.Crear.as_view(), name='crear'),
    
]