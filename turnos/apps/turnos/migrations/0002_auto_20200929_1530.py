# Generated by Django 3.0 on 2020-09-29 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0002_auto_20200929_1530'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnos',
            name='DNI',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turno_usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='turnos',
            name='id_local',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turno_idLocal', to='empresa.Empresa'),
        ),
        migrations.AddField(
            model_name='turnos',
            name='invitado1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turno_invitado1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='turnos',
            name='invitado2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turno_invitado2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='turnos',
            name='invitado3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turno_invitado3', to=settings.AUTH_USER_MODEL),
        ),
    ]
