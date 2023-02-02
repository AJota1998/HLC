from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import render
from blog.models import Articulos


def despedida(request):
    return HttpResponse("Esta es la página de despedida")

def dameFecha(request):
    fecha_actual = datetime.datetime.now()

    documento = """
    <html>
    <body>
    <h2>
    La fecha y hora actual es: {}
    </h2>
    </body>
    </html>
    """.format(fecha_actual)

    return HttpResponse(documento)

def calculaEdadActual(request, edad, agno):
      periodo = agno - datetime.datetime.now().year 
      nueva_edad = edad + periodo
      documento = """
        <html>
        <body>
        <h2>
        En el año {} tendrás: {}
        </h2>
        </body>
        </html>
        """.format(agno, nueva_edad)

      return HttpResponse(documento)

def saludo(request):
      persona = Persona("Chema", "Durán")
      temas_del_curso = ["Formularios", "Modelos", "Vistas", "Despliegue"]
      fecha_actual = datetime.datetime.now()
      return render(request, "saludo.html", 
      {"nombre_persona":persona.nombre, 
      "apellido_persona":persona.apellido, 
      "fecha_actual":fecha_actual, 
      "temas" : temas_del_curso})


class Persona(object):
      def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def curso_django(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "curso_django.html", {"fecha_actual":fecha_actual})

def curso_python(request):
    fecha_actual = datetime.datetime.now()
    return render(request, "curso_python.html", {"fecha_actual":fecha_actual})


def crear_articulo(request, nombre, seccion, precio):
    articulo = Articulos.crear_articulo(nombre, seccion, precio)
    return render(request, "crear_articulo.html", {"articulo":articulo})

def todos_articulos(request) :
    articulos = Articulos.todos_articulos()
    return render(request, "mostrar_articulos.html", {"articulos":articulos})

def borrar_articulos(request, id) :
    Articulos.borrar_articulos(id)
    documento = """
        <html>
        <body>
        <h2>
        articulo borrado {}
        </h2>
        </body>
        </html>
        """.format(id)
    return HttpResponse(documento)

def actualizar_articulos(request, id, nombre, seccion, precio) :
    articulo = Articulos.actualizar_articulos(id, nombre, seccion, precio)
    return render(request, "crear_articulo.html", {"articulo": articulo})