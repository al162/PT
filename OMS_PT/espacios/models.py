from django.db import models

class Espacio(models.Model):
    nombre_spc = models.CharField(max_length=50)

class Producto(models.Model):
    nombre_prod = models.CharField(max_length=50)
    espacio_id = models.BigIntegerField()