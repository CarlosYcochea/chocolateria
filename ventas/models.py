from django.db import models

# Create your models here.

class Clientes(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido)
    
class Categorias(models.Model):
    id_categorias = models.AutoField(db_column='idCategorias',primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=40)
    def __str__(self):
        return str(self.nombre)    

class Ventas(models.Model):
    id_ventas = models.AutoField(db_column='idVentas',primary_key=True)
    rut = models.ForeignKey('Clientes', on_delete=models.CASCADE,db_column='rut')
    fechaventas = models.DateField(blank=False, null=False)
    total = models.FloatField(default=0.0,blank=False,null=False)
    def __str__(self):
        return str(self.fechaventas)

class Productos(models.Model):
    id_producto = models.AutoField(db_column='idProducto',primary_key=True)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=30)
    precio = models.FloatField(default=0.0,blank=False,null=False)
    id_categorias = models.ForeignKey('Categorias', on_delete=models.CASCADE, db_column='idCategorias')
    def __str__(self):
        return str(self.nombre)

class DetalleVentas(models.Model):
    id_detalle_ventas = models.AutoField(db_column='idDetalleVentas',primary_key=True)
    id_ventas = models.ForeignKey('Ventas', on_delete=models.CASCADE, db_column='idVentas')
    id_producto = models.ForeignKey('Productos', on_delete=models.CASCADE , db_column='idProducto')
    cantidad = models.IntegerField(blank=False,null=False)
    precio = models.FloatField(default=0.0,blank=False,null=False)
    def __str__(self):
        return str(self.cantidad)