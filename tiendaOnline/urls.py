from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('detalle-del-producto/<str:id>/',
         views.detalles_producto, name='detalles_producto'),
]
