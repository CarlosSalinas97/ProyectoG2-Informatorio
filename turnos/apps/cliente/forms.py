from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.usuarios.models import Usuario

from .models import Cliente

class ClienteForm(UserCreationForm):


	class Meta:
		model = Usuario 
		fields = ['username','email','first_name','last_name','password1','password2', 'DNI', 'cumpleanio']
