from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.empresa.models import Empresa
from django.db import transaction
from .models import Cliente

class EmpresaForm(UserCreationForm):


	class Meta:
		model = Duenio 
		fields = ['username','email','first_name','last_name','password1','password2', 'DNI', 'fecha_nacimiento']