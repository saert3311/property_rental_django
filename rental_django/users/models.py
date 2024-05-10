from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=9, unique=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    class Meta:
        ordering = ('rut',)

class Regiones(models.Model):
    nombre = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=3, null=True, blank=True)
    capital = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    nombre = models.CharField(max_length=100)
    cod_region = models.ForeignKey(Regiones,  on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    cod_provincia = models.ForeignKey(Provincia, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre