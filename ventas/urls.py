from django.urls import path
from .views import index, login, dashboard, clientes


urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('dashboard', dashboard, name='dashboard'),
    path('clientes', clientes, name='clientes'),
]