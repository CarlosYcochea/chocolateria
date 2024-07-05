from django.urls import path
from .views import index, login, dashboard, clientes, clientesAdd, clientes_del, clientes_findEdit, clientesUpdate


urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('dashboard', dashboard, name='dashboard'),
    path('clientes', clientes, name='clientes'),
    path('clientesAdd', clientesAdd, name='clientesAdd'),
    path('clientes_del/<str:pk>', clientes_del, name='clientes_del'),
    path('clientes_findEdit/<str:pk>', clientes_findEdit, name='clientes_findEdit'),
    path('clientesUpdate', clientesUpdate, name='clientesUpdate'),

]