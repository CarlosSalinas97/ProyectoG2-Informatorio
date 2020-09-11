from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Turnos
from .forms import AltaTurno

class SolicitarTurno(LoginRequiredMixin,CreateView):
	model = Turnos
	form_class = AltaTurno
	template_name = 'turnos/solicitarTurno.html'
	success_url = reverse_lazy('home')

# Create your views here.
@login_required
def ListarTurnos(request):
	context = {}
	todos = Turnos.objects.all()
	context['turnos'] = todos
	print(todos)

	return render(request,'turnos/listarTurnos.html',context)