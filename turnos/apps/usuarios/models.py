from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
	DNI = models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='DNI')
	fecha_nacimiento = models.DateField('Fecha de Nacimiento(DD/MM/AAAA)',null=True)
	email = models.EmailField('email address', unique=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	es_duenio = models.BooleanField(default=False,null=False, blank=True)
	
	
	