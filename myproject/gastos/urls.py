from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("nuevo_gasto", views.nuevo_gasto, name="nuevo_gasto"),
    path("nuevo_rubro", views.nuevo_rubro, name="nuevo_rubro"),
    path("ver_gastos", views.ver_gastos, name="ver_gastos"), 
    path("eliminar_gasto/<id>", views.eliminar_gasto, name="eliminar_gasto"),
    path("eliminar_rubro/<id>", views.eliminar_rubro, name="eliminar_rubro"),
    
]