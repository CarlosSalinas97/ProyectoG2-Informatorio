from django.views.generic import CreateView
from django import forms
from django.db import transaction

from apps.empresa.models import Empresa
from .models import Empresa

class EmpresaForm(forms.ModelForm):
	class Meta:
		model = Empresa 
		fields = '__all__'
		exclude = ['DNI']

class EmpresaModificar(forms.ModelForm):
	class Meta:
		model = Empresa
		fields = ['Direccion','Telefono','PaginaWeb','Email','HorarioPrimeroAbre','HorarioPrimeroCierra','HorarioSegundoAbre','HorarioSegundoCierra','Imagen','Cant_empleados']