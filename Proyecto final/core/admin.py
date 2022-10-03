from lib2to3.pgen2.token import RPAR
from django.contrib import admin
from . models import Empleados, Inventario, Utilidades, Proyectos, Producto
# Register your models here.

@admin.register(Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','Cargo','hora', 'hora2', 'show_image']

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ['categoria','fecha_ingreso', 'fecha_salida']


@admin.register(Proyectos)
class ProyectosAdmin(admin.ModelAdmin):
    list_display = ['nombre_proyecto','fecha_inicio', 'fecha_final', 'ciudad', 'descripcion']


@admin.register(Utilidades)
class UtilidadesAdmin(admin.ModelAdmin):
    list_display = ['nombre','marca', 'precio', 'cantidad', 'categoria', 'show_image', 'disponible']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'show_image']