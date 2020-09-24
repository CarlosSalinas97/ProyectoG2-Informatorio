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

#TRABAJAR CON PERMISOS DE TIPOS DE USUARIO 
class Modificar(LoginRequiredMixin, UpdateView):
	model = Empresa
	form_class = EmpresaModificar
	template_name = 'empresa/modificar.html'
	success_url = reverse_lazy('empresa:listarDuenio')

class Eliminar(LoginRequiredMixin, DeleteView):
	model = Empresa
	success_url = reverse_lazy('empresa:listarDuenio')

@login_required
def RegistrarEmpresa(request):
	if request.method == 'POST':
		form = EmpresaForm(request.POST)
		if form.is_valid():
			x = form.save(commit=False)
			x.DNI = request.user
			x.save()
			return HttpResponseRedirect('/')
	else:
		form = EmpresaForm()

	return render(request, 'empresa/registro_empresa.html',{'form': form})

#No esta en uso
""" def ListarEmpresas(request):
	context = {}
	todos = Empresa.objects.all()
	context['empresas'] = todos

	return render(request,'empresa/listar_empresas.html',context) """


def Filtros(request):
	context = {}
	rubros = Rubro.objects.all()
	context['rubros'] = rubros
	id_rubro = request.GET.get('filtro',None)

	if id_rubro:
		resultado = Empresa.objects.filter(Rubro = id_rubro)
		context['empresas'] = resultado
	else:
		todos = Empresa.objects.all()
		context['empresas'] = todos

	return render(request,'empresa/listar_empresas.html',context)

#Idem a la funcion de arriba, pero solo para los dueños. Buscar como simplificar con las restricciones de tipo de usuario
def FiltrosDuenio(request):
	context = {}
	rubros = Rubro.objects.all()
	context['rubros'] = rubros
	id_rubro = request.GET.get('filtro',None)

	if id_rubro:
		resultado = Empresa.objects.filter(Rubro = id_rubro)
		context['empresas'] = resultado
	else:
		todos = Empresa.objects.all()
		context['empresas'] = todos

	return render(request,'empresa/listar_empresas_duenio.html',context)


#Solo disponible para usuario con rol de Dueño
@login_required
def ListarTurnos(request):
	context = {}
	todos = Turnos.objects.all()
	context['turnos'] = todos
	print(todos)

	return render(request,'turnos/listarTurnos.html',context)