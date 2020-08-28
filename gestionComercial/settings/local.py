from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE':'sql_server.pyodbc',
        'NAME':'TurnosBD',
        'Trusted_Connection':'yes',
        'HOST':'localhost\SQLEXPRESS', #El nombre del servidor local de admin sql
        'OPTIONS':{
        	'driver':'SQL Server Native Client 11.0',
        }
    },
}
