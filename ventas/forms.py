from django import forms
from .models import Ventas, Categorias, Productos, DetalleVentas

class VentasForm(forms.ModelForm):
	class Meta:
		model = Ventas
		fields = ['rut', 'fechaventas', 'total']
		

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['nombre', 'descripcion']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'precio', 'id_categorias']

class DetalleVentasForm(forms.ModelForm):
    class Meta:
        model = DetalleVentas
        fields = ['id_ventas', 'id_producto', 'cantidad', 'precio']

