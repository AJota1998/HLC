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

    def crear_articulo(p_nombre, p_seccion, p_precio) :
        art = Articulos(nombre=p_nombre, seccion=p_seccion, precio=p_precio)
        art.save()
        return art

    def todos_articulos() : 
        todos = Articulos.objects.all()
        return todos

    def borrar_articulos(p_id) :
        Articulos.objects.get(id=p_id).delete()

    def actualizar_articulos(p_id, p_nombre, p_seccion, p_precio) :
        articulo = Articulos.objects.get(id=p_id)
        articulo.nombre = p_nombre
        articulo.seccion = p_seccion
        articulo.precio = p_precio
        articulo.save()
        return articulo


    def __str__(self) : 
        return '{} y su precio es {}'.format(self.nombre, self.precio)

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField(max_length=15)
    entregado = models.CharField(max_length=20)


# Create your models here.
