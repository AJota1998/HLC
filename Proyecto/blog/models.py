from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=75)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=9)

class Articulos(models.Model):
    nombre = models.CharField(max_length=50)
    seccion = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField(max_length=15)
    entregado = models.CharField(max_length=20)


# Create your models here.
