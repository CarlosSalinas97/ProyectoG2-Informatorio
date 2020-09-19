from django.db import models
from apps.usuarios.models import Usuario



class Autoevaluaciones(models.Model):
	clave = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='codigo')#Le digo explícitamente la clave del producto (de no hacerlo django lo hace de manera incremental -1,2,3,4,5,m-)
	BOOL_CHOICES = ((True, 'Sí'), (False, 'No'))
	fiebre = models.BooleanField()
	tos = models.BooleanField()
	diarrea = models.BooleanField(choices=BOOL_CHOICES)
	dolor_garganta = models.BooleanField(choices=BOOL_CHOICES)
	dificultad_respiratoria = models.BooleanField(choices=BOOL_CHOICES)
	dolor_muscular = models.BooleanField(choices=BOOL_CHOICES)
	cefalea = models.BooleanField(choices=BOOL_CHOICES)
	vomito = models.BooleanField(choices=BOOL_CHOICES)
	gusto_olfato = models.BooleanField(choices=BOOL_CHOICES)
	usuario_test = models.OneToOneField(Usuario,related_name = 'usuario_test', null=True, on_delete = models.SET_NULL)
	resultado = models.CharField(max_length=10)

	sintomas = (fiebre, tos, diarrea, dolor_garganta, dificultad_respiratoria, dolor_muscular, cefalea, vomito, gusto_olfato)

	def resultado_covid(self):
		contador = 0
		for i in self.sintomas:
			if i:
				contador +=1

		if contador > 2 or self.gusto_olfato:
			self.resultado = "True"
		else:
			self.resultado = "False"