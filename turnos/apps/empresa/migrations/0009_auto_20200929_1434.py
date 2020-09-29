# Generated by Django 3.0 on 2020-09-29 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empresa', '0008_auto_20200923_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='DNI',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresa_usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
