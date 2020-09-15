#
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .forms import ModificarUsuario
from .models import Usuario


class Modificar(UpdateView):
	model = Usuario
	form_class = ModificarUsuario
	template_name = 'usuarios/modificarUsuario.html'
	success_url = reverse_lazy('home')
