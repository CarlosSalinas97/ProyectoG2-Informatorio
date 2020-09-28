# Generated by Django 3.0 on 2020-09-28 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0008_auto_20200923_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id_turno', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.DateField()),
                ('horario', models.CharField(choices=[('1', '8 a 10'), ('2', '10 a 13'), ('3', '17 a 20'), ('4', '20 a 00')], max_length=1)),
                ('DNI', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turno_usuario', to=settings.AUTH_USER_MODEL)),
                ('id_local', models.ManyToManyField(related_name='turno_idLocal', to='empresa.Empresa')),
                ('invitado1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turno_invitado1', to=settings.AUTH_USER_MODEL)),
                ('invitado2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turno_invitado2', to=settings.AUTH_USER_MODEL)),
                ('invitado3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='turno_invitado3', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
