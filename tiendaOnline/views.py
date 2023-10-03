from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from . models import *


def inicio(request):
    data = {
        "nombre": "Juanito",
        "productos": produstos(request),
    }
    return render(request, 'index.html', data)
    # return HttpResponse("Hola Mundo", status=200)
    # return render(request, 'index.html')


def produstos(request):
    return Producto.objects.all()


def detalles_producto(request, id):
    try:
        producto = Producto.objects.get(id=id)
        data = {"producto": producto}
        return render(request, "detalles.html", data)
    except Producto.DoesNotExist:
        # Manejar el caso en el que no existe el registro
        error_message = f"no existe ningún registro para la busqueda id: {id}"
        return render(request, "index.html", {"error_message": error_message})
