from django.db import models

from localflavor.ar.ar_provinces import PROVINCE_CHOICES 
from model_utils.fields import StatusField
from model_utils import Choices
from geoposition.fields import GeopositionField


# Create your models here.

class Siniestro(models.Model):
    STATUS = Choices('a_confirmar', 'confirmado', 'reportado')
    status = StatusField()

    causa_principal = models.ForeignKey('Causa')
    fecha = models.DateField()
    hora = models.TimeField(null=True)
    lugar = models.CharField(max_length=200, help_text='La dirección aproximada del siniestro. Ej: Ruta 5, Km 123')
    provincia = models.CharField(max_length=20, choices=PROVINCE_CHOICES)
    posicion = GeopositionField()
    mensaje = models.TextField(null=True)
    referencias_prensa = models.ManyToManyField('ReferenciaPrensa')
    cargado_por = models.ForeignKey('auth.User', editable=False, null=True)


class Causa(models.Model):
    causa = models.CharField(max_length=50)

    def __str__(self):
        return self.causa


class Victima(models.Model):
    GENEROS = Choices('masculino', 'femenino', 'otro')
    siniestro = models.ForeignKey('Siniestro')
    apellido = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    fecha = models.DateField(help_text='En ocasiones, una victima puede fallecer dias despues del siniestro')
    dni = models.CharField(max_length=10, null=True)
    nacionalidad = models.CharField(max_length=50, default='argentina')
    lugar_residencia = models.CharField(max_length=50, help_text='Donde vivia esta persona')
    genero = models.CharField(max_length=30, choices=GENEROS)
    fecha_nacimiento = models.DateField(null=True)
    fotos = models.ManyToManyField('ReferenciaPrensa')


class ReferenciaPrensa(models.Model):
    url = models.URLField(unique=True)
    

class Foto(models.Model):
    archivo = models.ImageField()


