from .models import Turnos
from django import forms

class AltaTurno(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = ['dia','invitado1','invitado2','invitado3']
        widgets = {
            'invitado1': forms.TextInput(attrs={'maxlength': "8"}),
            'invitado2': forms.TextInput(attrs={'maxlength': "8"}),
            'invitado3': forms.TextInput(attrs={'maxlength': "8"}),
        }