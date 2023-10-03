from django.contrib import admin

# Register your models here.

# Registrando mis Modelos
from . models import Producto, Categoria

# La función admin.site.register() se utiliza para registrar un modelo en el panel de administración de Django,
# Registrando los Modelos
admin.site.register(Producto)
admin.site.register(Categoria)
