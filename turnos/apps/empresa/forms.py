from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.empresa.models import Empresa
from django.db import transaction
from .models import Cliente

class EmpresaForm(UserCreationForm):


	class Meta:
		model = Empresa 
		fields = ['CUIT', 'DNI', 'Nombre', 'Razon_Social', 'Superficie', 'Cant_empleados']
