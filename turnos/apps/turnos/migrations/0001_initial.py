# Generated by Django 3.0 on 2020-09-29 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id_turno', models.AutoField(primary_key=True, serialize=False)),
                ('dia', models.DateField()),
                ('horario', models.CharField(choices=[('1', '8 a 10'), ('2', '10 a 13'), ('3', '17 a 20'), ('4', '20 a 00')], max_length=1)),
            ],
        ),
    ]
