from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Empresa, Rubro
from .forms import EmpresaForm, EmpresaModificar
from apps.turnos.models import Turnos
from apps.utils.funciones import PermisosMixin



#TRABAJAR CON PERMISOS DE TIPOS DE USUARIO 
class Modificar(LoginRequiredMixin, PermisosMixin, UpdateView):
	rol = 'duenio'
	model = Empresa
	form_class = EmpresaModificar
	template_name = 'empresa/modificar.html'
	success_url = reverse_lazy('empresa:listar')


class Eliminar(LoginRequiredMixin, PermisosMixin, DeleteView):
	rol = 'duenio'
	model = Empresa
	success_url = reverse_lazy('empresa:listar')


@login_required
def RegistrarEmpresa(request):
	if request.method == 'POST':
		form = EmpresaForm(request.POST, request.FILES)
		form.is_valid()
		print('------------------------------------------')
		print(form.errors)
		print('------------------------------------------')
		if form.is_valid():
			x = form.save(commit=False)
			x.DNI = request.user
			x.save()
			return HttpResponseRedirect('/')
	else:
		form = EmpresaForm()
		

	return render(request, 'empresa/registro_empresa.html',{'form': form})


def Filtros(request):
	context = {}
	rubros = Rubro.objects.all()
	context['rubros'] = rubros
	usuario = request.user
	id_rubro = request.GET.get('filtro',None)

	if id_rubro:
		resultado = Empresa.objects.filter(Rubro = id_rubro)
		context['empresas'] = resultado
	else:
		todos = Empresa.objects.all()
		context['empresas'] = todos

	if usuario.es_duenio:
		return render(request,'empresa/listar_empresas_duenio.html',context)
	else:
		return render(request,'empresa/listar_empresas.html',context)


#Solo disponible para usuario con rol de Dueño
@login_required
def ListarTurnos(request):
	usuario = request.user
	context = {}
	todos = Turnos.objects.all()
	context['turnos'] = todos
	print(todos)

	if usuario.es_duenio:
		return render(request,'turnos/listarTurnos.html',context)
	else:
		return render(request,'turnos/listarTurnos.html',context)