from django.shortcuts import render, redirect
from .models import Clientes, Categorias, Ventas, DetalleVentas, Productos
from .forms import VentasForm, CategoriaForm, ProductoForm, DetalleVentasForm
from django.http import HttpResponse


# Create your views here.

def index(request):

    return render(request, 'ventas/index.html')

def login(request):

    return render(request, 'ventas/login.html')

def dashboard(request):

    return render(request, 'ventas/dashboard.html')

def clientes(request):  
    clientes = Clientes.objects.all()
    context = {"clientes" :clientes}
    return render(request, 'ventas/clientes.html',context)

def clientesAdd(request):
    if  request.method !="POST":
        
        ventas = Ventas.objects.all()
        context={'ventas':ventas}
        return render(request, 'ventas/clientes_add.html', context)
    elif  request.method =="POST":



        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]

        obj=Clientes.objects.create(  rut=rut,
                                    nombre=nombre,
                                    apellido=apellido,
                                    telefono=telefono,
                                    email=email
                                    )
        obj.save()
        context={'mensaje':"OK, datos grabados..."}
        return render(request, 'ventas/clientes_add.html', context)
    
def clientes_del(request,pk):
    context={}
    try:
        cliente=Clientes.objects.get(rut=pk)

        cliente.delete()
        mensaje="Bien, datos eliminados..."
        clientes = Clientes.objects.all()
        context = {'clientes': clientes,  'mensaje' : mensaje}
        return render(request, 'ventas/clientes.html', context)
    except:
        mensaje="Error, rut no existe..."
        clientes = Clientes.objects.all()
        context = {'clientes': clientes,  'mensaje' : mensaje}
        return render(request, 'ventas/clientes.html', context)

def clientes_findEdit(request,pk):

    if pk != "":
        cliente=Clientes.objects.get(rut=pk)


        context={'cliente':cliente}
        if cliente:
            return render(request, 'ventas/clientes_edit.html', context)
        else:
            context={'mensaje':"Error, rut no existe..."}
            return render(request, 'ventas/clientes.html', context)
        

def clientesUpdate(request):

    if request.method == "POST":


        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]


        cliente = Clientes()
        cliente.rut=rut
        cliente.nombre=nombre
        cliente.apellido=apellido
        cliente.telefono=telefono
        cliente.email=email
        cliente.save()

        context={'mensaje':"Ok, datos actualizados...",'cliente':cliente }
        return render(request, 'ventas/clientes_edit.html', context)
    else:

        clientes = Clientes.objects.all()
        context={'clientes':clientes}
        return render(request, 'ventas/clientes_edit.html', context)

def ventas(request):
    ventas = Ventas.objects.all()
    context = {"ventas" :ventas}
    return render(request, 'ventas/ventas.html',context)

def ventasAdd(request):
    print("estoy en controlador ventasAdd...")
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = VentasForm(request.POST)
        if form.is_valid():
            print("estoy en agregar, is_valid")
            form.save()


            form= VentasForm()

            context={'mensaje':"Ok, datos grabados...",'form':form}
            return render(request,"ventas/ventas_add.html", context)
    else:
        form = VentasForm()
        context={'form':form}
        return render(request,'ventas/ventas_add.html', context)

def ventas_del(request,pk):
    context={}
    try:
        venta=Ventas.objects.get(id_ventas=pk)

        venta.delete()
        mensaje="Bien, datos eliminados..."
        ventas = Ventas.objects.all()
        context = {'ventas': ventas,  'mensaje' : mensaje}
        return render(request, 'ventas/ventas.html', context)
    except:
        mensaje="Error, id no existe..."
        ventas = Ventas.objects.all()
        context = {'ventas': ventas,  'mensaje' : mensaje}
        return render(request, 'ventas/ventas.html', context)

def ventas_findEdit(request, pk):
    try:
        venta=Ventas.objects.get(id_ventas=pk)
        context={}
        if venta:
            print("Edit encontro el venta...")
            if request.method == "POST":
                print("edit, es un POST")
                form = VentasForm(request.POST,instance=venta)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'venta':venta, 'form':form, 'mensaje':mensaje}
                return render(request,'ventas/ventas_edit.html', context)
            else:

                print("edit, No es un POST")
                form = VentasForm(instance=venta)
                mensaje=""
                context = {'venta':venta, 'form':form, 'mensaje':mensaje}
                return render(request,'ventas/ventas_edit.html', context)
    except:
        print("Error, id no existe...")
        venta= VentasForm.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje,'venta':venta}
        return render(request, 'ventas/ventas.html', context)
        
def ventasUpdate(request):

    if request.method == "POST":


        fecha=request.POST["fechaventas"]
        total=request.POST["total"]
        nombre=request.POST["rut"]

        objcliente=Clientes.objects.get(rut=nombre)

        venta = Ventas()
        venta.fechaventas=fecha
        venta.total=total
        venta.rut=objcliente
        venta.save()

        clientes = Clientes.objects.all()
        context={'mensaje':"Ok, datos actualizados...",'venta':venta, 'clientes':clientes}
        return render(request, 'ventas/ventas_edit.html', context)
    else:

        ventas = Ventas.objects.all()
        context={'ventas':ventas}
        return render(request, 'ventas/ventas_edit.html', context)

def categorias(request):
    categorias = Categorias.objects.all()
    context = {"categorias" :categorias}
    return render(request, 'ventas/categorias.html',context)

def categoriasAdd(request):
    print("estoy en controlador generosAdd...")
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = CategoriaForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()


            form=CategoriaForm()

            context={'mensaje':"Ok, datos grabados...",'form':form}
            return render(request,"ventas/categorias_add.html", context)
    else:
        form = CategoriaForm()
        context={'form':form}
        return render(request,'ventas/categorias_add.html', context)

def categorias_del(request, pk):
    context={}
    try:
        categoria = Categorias.objects.get(id_categorias=pk)

        categoria.delete()
        mensaje="Bien, datos eliminados..."
        categorias = Categorias.objects.all()
        context = {'categorias':categorias,  'mensaje' : mensaje}
        return render(request, 'ventas/categorias.html', context)
    except:
        mensaje="Error, rut no existe..."
        categorias = Categorias.objects.all()
        context = {'categorias':categorias,  'mensaje' : mensaje}
        return render(request, 'ventas/categorias.html', context)
    
def categorias_findEdit(request, pk):
    try:
        categoria=Categorias.objects.get(id_categorias=pk)
        context={}
        if categoria:
            print("Edit encontro el categoria...")
            if request.method == "POST":
                print("edit, es un POST")
                form = CategoriaForm(request.POST,instance=categoria)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'categoria':categoria, 'form':form, 'mensaje':mensaje}
                return render(request,'ventas/categorias_edit.html', context)
            else:

                print("edit, No es un POST")
                form = CategoriaForm(instance=categoria)
                mensaje=""
                context = {'categoria':categoria, 'form':form, 'mensaje':mensaje}
                return render(request,'ventas/categorias_edit.html', context)
    except:
        print("Error, id no existe...")
        categoria= CategoriaForm.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje,'categoria':categoria}
        return render(request, 'ventas/categorias.html', context)
    
def categoriasUpdate(request):

    if request.method == "POST":


        nombre=request.POST["nombre"]
        descripcion=request.POST["descripcion"]


        categoria = Categorias()
        categoria.nombre=nombre
        categoria.descripcion=descripcion
        categoria.save()

        context={'mensaje':"Ok, datos actualizados...",'categoria':categoria }
        return render(request, 'ventas/categorias_edit.html', context)
    else:

        categorias = Categorias.objects.all()
        context={'categorias':categorias}
        return render(request, 'ventas/categorias_edit.html', context) 

def productos(request):
    productos = Productos.objects.all()
    context = {"productos" :productos}
    return render(request, 'ventas/productos.html',context)

def productosAdd(request):
    print("estoy en controlador productosAdd...")
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = ProductoForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()


            form= ProductoForm()

            context={'mensaje':"Ok, datos grabados...",'form':form}
            return render(request,"ventas/productos_add.html", context)
    else:
        form = ProductoForm()
        context={'form':form}
        return render(request,'ventas/productos_add.html', context)

def productos_del(request, pk):
    context={}
    try:
        producto = Productos.objects.get(id_producto=pk)

        producto.delete()
        mensaje="Bien, datos eliminados..."
        productos = Productos.objects.all()
        context = {'productos':productos,  'mensaje' : mensaje}
        return render(request, 'ventas/productos.html', context)
    except:
        mensaje="Error, id no existe..."
        productos = Productos.objects.all()
        context = {'productos':productos,  'mensaje' : mensaje}
        return render(request, 'ventas/productos.html', context)

def productos_findEdit(request, pk):
    try:
        producto=Productos.objects.get(id_producto=pk)
        context={}
        if producto:
            print("Edit encontro el producto...")
            if request.method == "POST":
                print("edit, es un POST")
                form = ProductoForm(request.POST,instance=producto)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'producto':producto, 'form':form, 'mensaje':mensaje}
                return render(request,'ventas/productos_edit.html', context)
            else:

                print("edit, No es un POST")
                form = ProductoForm(instance=producto)
                mensaje=""
                context = {'producto':producto, 'form':form, 'mensaje':mensaje}
                return render(request,'ventas/productos_edit.html', context)
    except:
        print("Error, id no existe...")
        producto= ProductoForm.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje,'producto':producto}
        return render(request, 'ventas/productos.html', context)

def productosUpdate(request):

    if request.method == "POST":


        nombre=request.POST["nombre"]
        descripcion=request.POST["descripcion"]
        precio=request.POST["precio"]
        id_categorias=request.POST["id_categorias"]


        objcategoria=Categorias.objects.get(id_categorias=id_categorias)

        producto = Productos()
        producto.nombre=nombre
        producto.descripcion=descripcion
        producto.precio=precio
        producto.id_categorias=objcategoria
        producto.save()

        context={'mensaje':"Ok, datos actualizados...",'producto':producto }
        return render(request, 'ventas/productos_edit.html', context)
    else:

        productos = Productos.objects.all()
        context={'productos':productos}
        return render(request, 'ventas/productos_edit.html', context)

def detalles_ventas(request):
    detalles_ventas = DetalleVentas.objects.all()
    context = {"detalles_ventas" :detalles_ventas}
    return render(request, 'ventas/detalles_ventas.html',context)

def detalles_ventasAdd(request):
    print("estoy en controlador detalles_ventasAdd...")
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = DetalleVentasForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()


            form= DetalleVentasForm()

            context={'mensaje':"Ok, datos grabados...",'form':form}
            return render(request,"ventas/detalles_ventas_add.html", context)
    else:
        form = DetalleVentasForm()
        context={'form':form}
        return render(request,'ventas/detalles_ventas_add.html', context)

def detalles_ventas_del(request, pk):
    context={}
    try:
        detalle_ventas = DetalleVentas.objects.get(id_detalle_ventas=pk)

        detalle_ventas.delete()
        mensaje="Bien, datos eliminados..."
        detalles_ventas = DetalleVentas.objects.all()
        context = {'detalles_ventas':detalles_ventas,  'mensaje' : mensaje}
        return render(request, 'ventas/detalles_ventas.html', context)
    except:
        mensaje="Error, id no existe..."
        detalles_ventas = DetalleVentas.objects.all()
        context = {'detalles_ventas':detalles_ventas,  'mensaje' : mensaje}
        return render(request, 'ventas/detalles_ventas.html', context)

def detalles_ventas_findEdit(request, pk):
    try:
        detalle_ventas=DetalleVentas.objects.get(id_detalle_ventas=pk)
        context={}
        if detalle_ventas:
            print("Edit encontro el detalle_ventas...")
            if request.method == "POST":
                print("edit, es un POST")
                form = DetalleVentasForm(request.POST,instance=detalle_ventas)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'detalle_ventas':detalle_ventas, 'form':form, 'mensaje':mensaje}
                return render(request,'ventas/detalles_ventas_edit.html', context)
            else:

                print("edit, No es un POST")
                form = DetalleVentasForm(instance=detalle_ventas)
                mensaje=""
                context = {'detalle_ventas':detalle_ventas, 'form':form, 'mensaje':mensaje}
                return render(request,'ventas/detalles_ventas_edit.html', context)
    except:
        print("Error, id no existe...")
        detalle_ventas= DetalleVentasForm.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje,'detalle_ventas':detalle_ventas}
        return render(request, 'ventas/detalles_ventas.html', context)

def detalles_ventasUpdate(request):

    if request.method == "POST":


        id_ventas=request.POST["id_ventas"]
        id_producto=request.POST["id_producto"]
        cantidad=request.POST["cantidad"]
        precio=request.POST["precio"]


        objventas=Ventas.objects.get(id_ventas=id_ventas)
        objproducto=Productos.objects.get(id_producto=id_producto)

        detalle_ventas = DetalleVentas()
        detalle_ventas.id_ventas=objventas
        detalle_ventas.id_producto=objproducto
        detalle_ventas.cantidad=cantidad
        detalle_ventas.precio=precio
        detalle_ventas.save()

        context={'mensaje':"Ok, datos actualizados...",'detalle_ventas':detalle_ventas }
        return render(request, 'ventas/detalles_ventas_edit.html', context)
    else:

        detalles_ventas = DetalleVentas.objects.all()
        context={'detalles_ventas':detalles_ventas}
        return render(request, 'ventas/detalles_ventas_edit.html', context)          
