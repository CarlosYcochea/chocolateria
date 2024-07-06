from django import forms
from .models import Ventas, Categorias

class VentasForm(forms.ModelForm):
	class Meta:
		model = Ventas
		fields = ['rut', 'fechaventas', 'total']
		

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categorias
        fields = ['nombre', 'descripcion']