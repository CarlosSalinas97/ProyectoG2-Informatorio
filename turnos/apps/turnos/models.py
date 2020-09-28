from django.db import models
from apps.usuarios.models import Usuario
from apps.empresa.models import Empresa

# Create your models here.
class Turnos(models.Model):
    OpcionHorarios = [
        ('1', '8 a 10'),
        ('2', '10 a 13'),
        ('3', '17 a 20'),
        ('4', '20 a 00'),
    ]
    id_turno = models.AutoField(primary_key = True)
    DNI = models.ForeignKey(Usuario, related_name = 'turno_usuario', null=True, on_delete = models.SET_NULL)
    id_local = models.ForeignKey(Empresa, related_name = 'turno_idLocal', null=True, on_delete = models.SET_NULL)
    dia = models.DateField()
    invitado1 = models.ForeignKey(Usuario, related_name = 'turno_invitado1', null=True, on_delete = models.SET_NULL, blank=True)
    invitado2 = models.ForeignKey(Usuario, related_name = 'turno_invitado2', null=True, on_delete = models.SET_NULL, blank=True)
    invitado3 = models.ForeignKey(Usuario, related_name = 'turno_invitado3', null=True, on_delete = models.SET_NULL, blank=True)
    horario = models.CharField(max_length=1, choices=OpcionHorarios)

    def MaximoTurnos(self, dni, id_local):
        print('-------------------------------------------')
        print('id_local:', id_local)
        print('Horario:', self.horario)
        print('Dia:', self.dia)
        print('DNI:', dni)
        print('-------------------------------------------')
        return True