from django.db import models
from apps.usuarios.models import Usuario

# Create your models here.
class Turnos(models.Model):
    id_turno = models.AutoField(primary_key = True)
    DNI = models.OneToOneField(Usuario,related_name = 'turno_usuario', null=True, on_delete = models.SET_NULL)
    id_local = models.PositiveIntegerField()
    dia = models.DateField()
    invitado1 = models.OneToOneField(Usuario,related_name = 'turno_invitado1', null=True, on_delete = models.SET_NULL, blank=True)
    invitado2 = models.OneToOneField(Usuario,related_name = 'turno_invitado2', null=True, on_delete = models.SET_NULL, blank=True)
    invitado3 = models.OneToOneField(Usuario,related_name = 'turno_invitado3', null=True, on_delete = models.SET_NULL, blank=True)