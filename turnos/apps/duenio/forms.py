from django.contrib.auth.forms import UserCreationForm
from django import forms
from apps.usuarios.models import Usuario
from django.db import transaction
from .models import Duenio

class DuenioForm(UserCreationForm):

	CUIL = forms.IntegerField()

	class Meta:
		model = Usuario 
		fields = ['username','email','first_name','last_name','password1','password2', 'DNI', 'fecha_nacimiento']

	@transaction.atomic
	def save(self):
		usuario = super().save(commit=False)
		usuario.es_duenio = True
		usuario.save()
		Duenio.objects.create(usuario = usuario, CUIL = self.cleaned_data.get('CUIL'))
		return usuario