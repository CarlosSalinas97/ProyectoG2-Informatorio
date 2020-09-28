from .models import Turnos
from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

class AltaTurno(forms.ModelForm):
	class Meta:
		model = Turnos
		fields = ['dia','horario','invitado1','invitado2','invitado3']
		widgets = {
			'dia': DatePicker(
				options={
				'useCurrent': True,
				'collapse': False,
				},
				attrs={
				'append': 'fa fa-calendar',
				'icon_toggle': True,
				'autocomplete': 'off'
			}
			),
			'invitado1': forms.TextInput(attrs={'maxlength': "8", 'autocomplete': 'off'}),
			'invitado2': forms.TextInput(attrs={'maxlength': "8", 'autocomplete': 'off'}),
			'invitado3': forms.TextInput(attrs={'maxlength': "8", 'autocomplete': 'off'}),
		}