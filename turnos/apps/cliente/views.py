from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ClienteForm
from apps.usuarios.models import Usuario
from django.urls import reverse_lazy

# Create your views here.
class RegistroCliente(CreateView):
	model = Usuario
	form_class = ClienteForm
	template_name = 'cliente/registro_cliente.html'
	success_url = reverse_lazy('autoevaluacion:crearFuncion')
