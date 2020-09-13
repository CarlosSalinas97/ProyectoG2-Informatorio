from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
	dni = models.IntegerField(primary_key = True)
	cumpleanio = models.DateField()
	email = models.EmailField('email address', unique=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	
	
	