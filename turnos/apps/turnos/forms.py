from .models import Turnos
from django import forms

class AltaTurno(forms.ModelForm):
    class Meta:
        model = Turnos
        fields = '__all__'