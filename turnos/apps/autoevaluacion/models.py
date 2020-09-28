from django.db import models
from apps.usuarios.models import Usuario



class Autoevaluaciones(models.Model):
	
	BOOL_CHOICES = ((True, 'Sí'), (False, 'No'))
	fiebre = models.BooleanField(choices=BOOL_CHOICES)
	tos = models.BooleanField(choices=BOOL_CHOICES)
	diarrea = models.BooleanField(choices=BOOL_CHOICES)
	dolor_garganta = models.BooleanField(choices=BOOL_CHOICES)
	dificultad_respiratoria = models.BooleanField(choices=BOOL_CHOICES)
	dolor_muscular = models.BooleanField(choices=BOOL_CHOICES)
	cefalea = models.BooleanField(choices=BOOL_CHOICES)
	vomito = models.BooleanField(choices=BOOL_CHOICES)
	gusto_olfato = models.BooleanField(choices=BOOL_CHOICES)
	usuario_test = models.ForeignKey(Usuario, null=True, related_name = 'usuario_test', on_delete = models.SET_NULL)
	resultado = models.CharField(max_length=10)
	fecha_test = models.DateField()

	
	def resultado_covid(self):
		sintomas = (self.fiebre, self.tos, self.diarrea, self.dolor_garganta, self.dificultad_respiratoria, self.dolor_muscular, self.cefalea, self.vomito)
		contador = 0
		for i in sintomas:
			if i == True:
				contador += 1

		if contador > 2 or self.gusto_olfato:
			self.resultado = "True"
		else:
			self.resultado = "False"

	def Verificacion(self):
		if self.resultado == 'True':
			print('Positivo')
			return True
		else:
			print('Negativo')
			return False
