from django import forms
from .models import Autoevaluaciones


class AutoevaluacionForm(forms.ModelForm):

	class Meta:
		model = Autoevaluaciones
		fields = ['fiebre','tos','diarrea','dolor_garganta','dificultad_respiratoria','dolor_muscular','cefalea','vomito','gusto_olfato']
		widgets = { '__all__': forms.RadioSelect }