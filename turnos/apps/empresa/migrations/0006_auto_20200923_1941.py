# Generated by Django 3.0 on 2020-09-23 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_auto_20200923_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='CUIT',
            field=models.BigIntegerField(max_length=12, primary_key=True, serialize=False, verbose_name='CUIT'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='Cant_empleados',
            field=models.BigIntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='Superficie',
            field=models.BigIntegerField(max_length=3),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='Telefono',
            field=models.BigIntegerField(max_length=9),
        ),
    ]
