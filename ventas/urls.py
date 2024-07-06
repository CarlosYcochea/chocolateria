from django.urls import path
<<<<<<< HEAD
from .views import index, login, dashboard, clientes, clientesAdd, clientes_del, clientes_findEdit, clientesUpdate, ventas, ventasAdd, ventas_del, ventas_findEdit, ventasUpdate
=======
from .views import index, login, dashboard, clientes, clientesAdd, clientes_del, clientes_findEdit, clientesUpdate, categorias, categoriasAdd, categorias_findEdit, categorias_del, categoriasUpdate
>>>>>>> carlos


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

]