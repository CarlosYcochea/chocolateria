# Generated by Django 5.0.6 on 2024-07-05 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id_categorias', models.AutoField(db_column='idCategorias', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=45)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_producto', models.AutoField(db_column='idProducto', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=30)),
                ('precio', models.FloatField(default=0.0)),
                ('id_categorias', models.ForeignKey(db_column='idCategorias', on_delete=django.db.models.deletion.CASCADE, to='ventas.categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id_ventas', models.AutoField(db_column='idVentas', primary_key=True, serialize=False)),
                ('fechaventas', models.DateField()),
                ('total', models.FloatField(default=0.0)),
                ('rut', models.ForeignKey(db_column='rut', on_delete=django.db.models.deletion.CASCADE, to='ventas.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleVentas',
            fields=[
                ('id_detalle_ventas', models.AutoField(db_column='idDetalleVentas', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField(default=0.0)),
                ('id_producto', models.ForeignKey(db_column='idProducto', on_delete=django.db.models.deletion.CASCADE, to='ventas.productos')),
                ('id_ventas', models.ForeignKey(db_column='idVentas', on_delete=django.db.models.deletion.CASCADE, to='ventas.ventas')),
            ],
        ),
    ]