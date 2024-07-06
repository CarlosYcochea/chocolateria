from django.shortcuts import render, redirect
from .models import Clientes, Categorias, Ventas, DetalleVentas, Productos
from .forms import VentasForm


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
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ventas/ventas_add.html')
    else:
        form = VentasForm()
    return render(request, 'ventas/ventas_add.html', {'form': form})

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
        venta = Ventas.objects.get(id_ventas=pk)  # Asegúrate de que 'id' es el nombre correcto del campo clave primaria en tu modelo Ventas
        context = {}
        if venta:
            print("Edit encontró la venta...")
            if request.method == "POST":
                print("Edit, es un POST")
                form = VentasForm(request.POST, instance=venta)
                if form.is_valid():  # Asegúrate de validar el formulario antes de guardarlo
                    form.save()
                    mensaje = "Bien, datos actualizados..."
                    print(mensaje)
                    context = {'venta': venta, 'form': form, 'mensaje': mensaje}
                    return render(request, 'ventas/ventas_edit.html', context)
                else:
                    # En caso de que el formulario no sea válido, también deberías manejar esta situación
                    print("Formulario no válido")
                    mensaje = "Error, el formulario no es válido"
                    context = {'venta': venta, 'form': form, 'mensaje': mensaje}
                    return render(request, 'ventas/ventas_edit.html', context)
            else:
                print("Edit, No es un POST")
                form = VentasForm(instance=venta)
                mensaje = ""
                context = {'venta': venta, 'form': form, 'mensaje': mensaje}
                return render(request, 'ventas/ventas_edit.html', context)
    except Ventas.DoesNotExist:  # Es mejor capturar la excepción específica
        print("Error, id no existe...")
        ventas = Ventas.objects.all()
        mensaje = "Error, id no existe"
        context = {'mensaje': mensaje, 'ventas': ventas}
        return render(request, 'ventas/ventas_list.html', context)
        
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
    if  request.method !="POST":
        
        productos = Productos.objects.all()
        context={'productos':productos}
        return render(request, 'ventas/categorias_add.html', context)
    elif  request.method =="POST":



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
