from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.
class Cliente(models.Model):
	usuario = models.OneToOneField(Usuario, related_name = "usuario_cliente", on_delete = models.CASCADE)