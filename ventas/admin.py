from django.contrib import admin
from .models import Clientes, Categorias, Ventas, Productos, DetalleVentas

# Register your models here.

admin.site.register(Clientes)
admin.site.register(Categorias)
admin.site.register(Ventas)
admin.site.register(Productos)
admin.site.register(DetalleVentas)
