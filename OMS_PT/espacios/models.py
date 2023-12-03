from django.db import models

class Espacio(models.Model):
    nombre_spc = models.CharField(max_length=50)

class Producto(models.Model):
    nombre_prod = models.CharField(max_length=50, unique=True)
    espacio_id = models.BigIntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0)

class Orden(models.Model):
    codigo = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField(Producto, through= 'OrdenProducto')

class OrdenProducto(models.Model):
    cantidad = models.PositiveIntegerField()
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE) 
