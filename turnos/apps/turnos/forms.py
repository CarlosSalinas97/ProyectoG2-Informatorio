from .models import Turnos
from django import forms

class AltaTurno(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = '__all__'
        widgets = {
            'DNI': forms.TextInput(attrs={'required': True, 'maxlength': "8"}),
            'id_local': forms.TextInput(attrs={'required': True, 'maxlength': "8"}),
            'invitado1': forms.TextInput(attrs={'maxlength': "8"}),
            'invitado2': forms.TextInput(attrs={'maxlength': "8"}),
            'invitado3': forms.TextInput(attrs={'maxlength': "8"}),
        }