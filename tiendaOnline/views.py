from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


def inicio(request):
    data = {
        "nombre": "Juanito",
    }
    return render(request, 'index.html', data)
    # return HttpResponse("Hola Mundo", status=200)
    # return render(request, 'index.html')
