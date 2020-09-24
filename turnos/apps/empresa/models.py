from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.usuarios.models import Usuario

# Create your models here.
class Rubro(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

class Razon_Social(models.Model):
	nombre = models.CharField(max_length = 50)
	
	def __str__(self):
		return self.nombre

class Empresa(models.Model):
	CUIT = models.BigIntegerField(primary_key = True, serialize = False, verbose_name = 'CUIT')
	DNI = models.OneToOneField(Usuario, related_name = "empresa_usuario", on_delete = models.CASCADE)
	Nombre = models.CharField(max_length = 50)
	Razon_Social = models.ForeignKey(Razon_Social, related_name = "razon_social", on_delete = models.CASCADE)
	Direccion = models.CharField(max_length = 80)
	Telefono = models.BigIntegerField(null = True,blank=True)
	PaginaWeb = models.CharField(max_length = 150,null = True,blank=True)
	Email = models.CharField(max_length = 50,null = True,blank=True)
	HorarioPrimeroAbre = models.CharField(max_length = 50,null = True,blank=True)
	HorarioPrimeroCierra = models.CharField(max_length = 50,null = True,blank=True)
	HorarioSegundoAbre = models.CharField(max_length = 50,null = True,blank=True)
	HorarioSegundoCierra = models.CharField(max_length = 50,null = True,blank=True)
	Imagen = models.ImageField(upload_to="empresa",null = True,blank=True)
	Superficie = models.BigIntegerField()
	Cant_empleados = models.BigIntegerField()
	Rubro = models.ForeignKey(Rubro, related_name = "rubro_empresa", on_delete = models.CASCADE)

	def __str__(self):
		return self.Nombre