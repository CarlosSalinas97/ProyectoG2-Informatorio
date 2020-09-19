from django.shortcuts import render
from django.views.generic import CreateView
from .forms import DuenioForm
from apps.usuarios.models import Usuario
from django.urls import reverse_lazy

# Create your views here.
class RegistroDuenio(CreateView):
	model = Usuario
	form_class = DuenioForm
	template_name = 'duenio/registro_duenio.html'
	success_url = reverse_lazy('home')
