from django.db import models

# Create your models here.
class Turnos(models.Model):
    id_turno = models.AutoField(primary_key = True)
    #FKUsuario
    DNI = models.PositiveIntegerField()
    #FKLocal
    id_local = models.PositiveIntegerField()
    dia = models.DateField()
    #FKUsuario
    invitado1 = models.PositiveIntegerField(null = True, blank = True)
    #FKUsuario
    invitado2 = models.PositiveIntegerField(null = True, blank = True)
    #FKUsuario
    invitado3 = models.PositiveIntegerField(null = True, blank = True)