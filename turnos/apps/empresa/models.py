from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.usuario.models import Usuario

# Create your models here.
class Razon_Social():
	nombre = models.CharFIeld(max_lenght = 50)
	#completar con los tipos de razon social
	pass

class Empresa(models.Model, Razon):
	CUIT = models.PositiveIntegerField(primary_key = True, serialize = False, verbose_name = 'CUIT')
	DNI = models.OneToOneField(Usuario, related_name = "empresa_usuario", on_delete = models.CASCADE)
	Nombre = models.CharField(max_length = 50)
	Razon_Social = models.ForeignKey(Razon_Social, related_name = "razon_social", on_delete = models.CASCADE)
	Superficie = models.PositiveIntegerField()
	Cant_empleados = models.PositiveIntegerField()
