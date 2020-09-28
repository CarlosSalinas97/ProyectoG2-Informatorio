from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, ModelFormMixin
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from datetime import date

from .models import Turnos
from .forms import AltaTurno
from apps.utils.funciones import PermisosMixin
from apps.empresa.models import Empresa
from apps.autoevaluacion.models import Autoevaluaciones
from apps.autoevaluacion.forms import AutoevaluacionForm


@login_required
def ListarTurnos(request, pk):
	context = {}
	todos = Turnos.objects.filter(id_local = pk)
	context['turnos'] = todos
	return render(request,'turnos/listarTurnos.html',context)


@login_required
def ListarTurnosClientes(request):
	usuario = request.user
	context = {}
	todos = Turnos.objects.filter(DNI = usuario)
	context['turnos'] = todos
	return render(request,'turnos/listarTurnos.html',context)


@login_required
def SolicitarTurno(request, pk):
	print('--------------------------------------')
	a = Autoevaluaciones.objects.get(usuario_test = request.user.DNI)
	print(a.resultado)
	print(a.fecha_test)
	print(date.today())
	resta = str((date.today())-(a.fecha_test))
	if resta == '7 days, 0:00:00':
		print('Anduvo')
	else:
		print('error')
		
	print('--------------------------------------')
	#Comparar que el resultado sea False y la fecha no sea superior a 7 días de haberse realizado
	#Si supera los 7 días, eliminar la autoevaluacion y redireccionarle para que la realice de nuevo
	if request.method == 'POST':
		form = AltaTurno(request.POST)
		if form.is_valid():
			x = form.save(commit=False)
			x.DNI = request.user
			x.id_local = Empresa.objects.get(CUIT = pk)
			x.save()
			return HttpResponseRedirect('/')
	else:
		form = AltaTurno()

	return render(request, 'turnos/solicitarTurno.html',{'form': form})