from django.db import models
from apps.usuarios.models import Usuario
from apps.empresa.models import Empresa

# Create your models here.
class Turnos(models.Model):
    id_turno = models.AutoField(primary_key = True)
    DNI = models.OneToOneField(Usuario,related_name = 'turno_usuario', null=True, on_delete = models.SET_NULL)
    id_local = models.OneToOneField(Empresa,related_name = 'turno_idLocal', on_delete = models.SET_NULL, null=True)
    dia = models.DateField()
    invitado1 = models.OneToOneField(Usuario,related_name = 'turno_invitado1', null=True, on_delete = models.SET_NULL, blank=True)
    invitado2 = models.OneToOneField(Usuario,related_name = 'turno_invitado2', null=True, on_delete = models.SET_NULL, blank=True)
    invitado3 = models.OneToOneField(Usuario,related_name = 'turno_invitado3', null=True, on_delete = models.SET_NULL, blank=True)