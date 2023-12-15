from django.db import models

class Mesa(models.Model):
    numero = models.IntegerField()
    size = models.CharField(max_length=50)
    min_sillas = models.IntegerField()
    max_sillas = models.IntegerField()

class Reserva(models.Model):
    mesa_id = models.IntegerField()
    user_id = models.IntegerField()
    fecha = models.DateTimeField()
    sillas = models.IntegerField()