from django.contrib import admin
from .models import Empresa, Rubro, Razon_Social

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Rubro)
admin.site.register(Razon_Social)