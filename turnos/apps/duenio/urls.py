from django.contrib import admin
from django.urls import path
from . import views

app_name = 'duenio'
urlpatterns = [
    path('RegistrarDuenio/',views.RegistroDuenio.as_view(), name = "registrar_duenio"),

]