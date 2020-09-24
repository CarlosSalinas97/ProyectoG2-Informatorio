from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, ModelFormMixin
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Turnos
from .forms import AltaTurno
from apps.utils.funciones import PermisosMixin
from apps.empresa.models import Empresa

class SolicitarTurno(LoginRequiredMixin, PermisosMixin, CreateView):
	rol = 'cliente'
	model = Turnos
	form_class = AltaTurno
	template_name = 'turnos/solicitarTurno.html'
	success_url = reverse_lazy('home')


@login_required
def ListarTurnos(request):
	context = {}
	todos = Turnos.objects.all()
	context['turnos'] = todos
	print(todos)

	return render(request,'turnos/listarTurnos.html',context)

@login_required
def CrearEvaluacion(request, pk):
	if request.method == 'POST':
		form = AltaTurno(request.POST)
		if form.is_valid():
			x = form.save(commit=False)
			x.DNI = request.user
			
			#x.id_local = Empresa.objects.filter(CUIT = pk)
			x.save()
			return HttpResponseRedirect('/')
	else:
		form = AltaTurno()
		context = {}
		empresas = Empresa.objects.all()
		context['empresas'] = empresas
		print(context)

	return render(request, 'turnos/solicitarTurno.html',{'form': form})