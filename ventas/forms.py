from django import forms
<<<<<<< HEAD
from .models import Ventas, Categorias
=======
from .models import Ventas, Categorias, Productos, DetalleVentas
>>>>>>> 77a67a8ae91b03d3a3c69b7471f03bf24bb77824

class VentasForm(forms.ModelForm):
	class Meta:
		model = Ventas
		fields = ['rut', 'fechaventas', 'total']
		

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
<<<<<<< HEAD
        fields = ['nombre', 'descripcion']
=======
        fields = ['nombre', 'descripcion']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'precio', 'id_categorias']

class DetalleVentasForm(forms.ModelForm):
    class Meta:
        model = DetalleVentas
        fields = ['id_ventas', 'id_producto', 'cantidad', 'precio']

>>>>>>> 77a67a8ae91b03d3a3c69b7471f03bf24bb77824
