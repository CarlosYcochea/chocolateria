from django.shortcuts import render
from .models import Clientes, Categorias, Ventas, DetalleVentas, Productos

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

<<<<<<< HEAD
def ventas(request):
    ventas = Ventas.objects.all()
    context = {"ventas" :ventas}
    return render(request, 'ventas/ventas.html',context)

def ventasAdd(request):
=======
def categorias(request):
    categorias = Categorias.objects.all()
    context = {"categorias" :categorias}
    return render(request, 'ventas/categorias.html',context)

def categoriasAdd(request):
>>>>>>> carlos
    if  request.method !="POST":
        
        productos = Productos.objects.all()
        context={'productos':productos}
<<<<<<< HEAD
        return render(request, 'ventas/ventas_add.html', context)
=======
        return render(request, 'ventas/categorias_add.html', context)
>>>>>>> carlos
    elif  request.method =="POST":



<<<<<<< HEAD
        fecha=request.POST["fecha"]
        total=request.POST["total"]
        cliente=request.POST["cliente"]


        objcliente=Clientes.objects.get(rut=cliente)
        obj=Ventas.objects.create(  fecha=fecha,
                                    total=total,
                                    cliente=objcliente
                                    )
        obj.save()
        context={'mensaje':"OK, datos grabados..."}
        return render(request, 'ventas/ventas_add.html', context)

def ventas_del(request,pk):
    context={}
    try:
        venta=Ventas.objects.get(id=pk)

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

def ventas_findEdit(request,pk):

    if pk != "":
        venta=Ventas.objects.get(id=pk)
        clientes = Clientes.objects.all()


        context={'venta':venta, 'clientes':clientes}
        if venta:
            return render(request, 'ventas/ventas_edit.html', context)
        else:
            context={'mensaje':"Error, id no existe..."}
            return render(request, 'ventas/ventas.html', context)
        
def ventasUpdate(request):
=======
        nombre=request.POST["nombre"]
        descripcion=request.POST["descripcion"]

        obj=Categorias.objects.create(nombre=nombre,
                                    descripcion=descripcion,
                                    )
        obj.save()
        context={'mensaje':"OK, datos grabados..."}
        return render(request, 'ventas/categorias_add.html', context)

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

     if pk != "":
        categoria=Categorias.objects.get(id_categorias=pk)


        context={'categoria':categoria}
        if categoria:
            return render(request, 'ventas/categorias_edit.html', context)
        else:
            context={'mensaje':"Error, rut no existe..."}
            return render(request, 'ventas/categorias.html', context)

def categoriasUpdate(request):
>>>>>>> carlos

    if request.method == "POST":


<<<<<<< HEAD
        fecha=request.POST["fecha"]
        total=request.POST["total"]
        cliente=request.POST["cliente"]

        objcliente=Clientes.objects.get(rut=cliente)

        venta = Ventas()
        venta.fecha=fecha
        venta.total=total
        venta.cliente=objcliente
        venta.save()

        clientes = Clientes.objects.all()
        context={'mensaje':"Ok, datos actualizados...",'venta':venta, 'clientes':clientes}
        return render(request, 'ventas/ventas_edit.html', context)
    else:

        ventas = Ventas.objects.all()
        context={'ventas':ventas}
        return render(request, 'ventas/ventas_edit.html', context)        
=======
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
>>>>>>> carlos
