from django.urls import path
from .views import index, login, dashboard, clientes, clientesAdd, clientes_del, clientes_findEdit, clientesUpdate, ventas, ventasAdd, ventas_del, ventas_findEdit, ventasUpdate, categorias, categoriasAdd, categorias_del, categorias_findEdit, categoriasUpdate, productos, productosAdd, productos_del, productos_findEdit, productosUpdate, detalles_ventas, detalles_ventasAdd, detalles_ventas_del, detalles_ventas_findEdit, detalles_ventasUpdate


urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('dashboard', dashboard, name='dashboard'),
    path('clientes', clientes, name='clientes'),
    path('clientesAdd', clientesAdd, name='clientesAdd'),
    path('clientes_del/<str:pk>', clientes_del, name='clientes_del'),
    path('clientes_findEdit/<str:pk>', clientes_findEdit, name='clientes_findEdit'),
    path('clientesUpdate', clientesUpdate, name='clientesUpdate'),
    path('ventas', ventas, name='ventas'),
    path('ventasAdd', ventasAdd, name='ventasAdd'),
    path('ventas_del/<str:pk>', ventas_del, name='ventas_del'),
    path('ventas_findEdit/<str:pk>', ventas_findEdit, name='ventas_findEdit'),
    path('ventasUpdate', ventasUpdate, name='ventasUpdate'),
    path('categorias', categorias, name='categorias'),
    path('categoriasAdd', categoriasAdd, name='categoriasAdd'),
    path('categorias_del/<str:pk>', categorias_del, name='categorias_del'),
    path('categorias_findEdit/<str:pk>', categorias_findEdit, name='categorias_findEdit' ),
    path('categoriasUpdate', categoriasUpdate, name='categoriasUpdate'),
    path('productos', productos, name='productos'),
    path('productosAdd', productosAdd, name='productosAdd'),
    path('productos_del/<str:pk>', productos_del, name='productos_del'),
    path('productos_findEdit/<str:pk>', productos_findEdit, name='productos_findEdit'),
    path('productosUpdate', productosUpdate, name='productosUpdate'),
    path('detalles_ventas', detalles_ventas, name='detalles_ventas'),
    path('detalles_ventasAdd', detalles_ventasAdd, name='detalles_ventasAdd'),
    path('detalles_ventas_del/<str:pk>', detalles_ventas_del, name='detalles_ventas_del'),
    path('detalles_ventas_findEdit/<str:pk>', detalles_ventas_findEdit, name='detalles_ventas_findEdit'),
    path('detalles_ventasUpdate', detalles_ventasUpdate, name='detalles_ventasUpdate'),
    


]