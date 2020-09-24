from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.
class Duenio(models.Model):
	usuario = models.OneToOneField(Usuario, related_name = "usuario_duenio", on_delete = models.CASCADE)
	CUIL = models.BigIntegerField()

	def __str__(self):
		return self.CUIL