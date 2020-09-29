from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, ModelFormMixin
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from datetime import date, datetime

from .models import Turnos
from .forms import AltaTurno
from apps.utils.funciones import PermisosMixin
from apps.empresa.models import Empresa
from apps.autoevaluacion.models import Autoevaluaciones
from apps.autoevaluacion.forms import AutoevaluacionForm
from apps.autoevaluacion.views import CrearEvaluacion


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
	evaluacion = Autoevaluaciones.objects.get(usuario_test = request.user.DNI)
	#Controla que el cliente no tenga un testPositivo asignado
	if evaluacion.fecha_testPositivo == None:
		resta = (date.today()-evaluacion.fecha_test).days
	else:
		resta = (date.today()-evaluacion.fecha_testPositivo).days
		if resta == 0:
			pass
		else:
			#Informar que no puede entrar
			return HttpResponseRedirect('/')

	#El cliente no tiene un testPositivo asignado
	#Controla que el test se encuentre realizado hace como mucho 7 días. Caso contrario, lo redirije a realizar un nuevo test
	if resta > 7:
		#Se borra la evaluacion anterior
		evaluacion.delete()
		#Tiene que rehacer la autoevaluacion
		CrearEvaluacion()
	else:
		#Controla que el test haya resultado negativo. Puede proceder a sacar un turno
		if evaluacion.resultado == 'False':
			empresa = Empresa.objects.get(CUIT = pk)
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

			return render(request, 'turnos/solicitarTurno.html',{'form': form, 'empresa': empresa})
		#Si el test es positivo, se le asigna 2 semanas de exclución para solicitar turnos.
		else:
			#No puede solicitar turnos por 14 dias
			evaluacion.fecha_testPositivo = evaluacion.fecha_test + datetime.timedelta(days=14)
			evaluacion.save()
			#Informar lo sucedido
			return HttpResponseRedirect('/')
