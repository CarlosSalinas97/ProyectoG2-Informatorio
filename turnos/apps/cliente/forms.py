from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.usuarios.models import Usuario
from django.db import transaction

from .models import Cliente

class ClienteForm(UserCreationForm):


	class Meta:
		model = Usuario 
		fields = ['username','email','first_name','last_name','password1','password2', 'DNI', 'fecha_nacimiento']

	@transaction.atomic
	def save(self):
		usuario = super().save(commit = False)
		usuario.save()
		Cliente.objects.create(usuario=usuario)
		return usuario
