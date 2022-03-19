from django.shortcuts import render
from django.http import HttpResponse

from almacen.models import Cliente, Proveedor, Producto
from .forms import Busqueda, ClienteForm, ProveedorForm, ProductoForm

# Create your views here.

def inicio(request):
    context = {}
    return render(request, "tmp_index.html", context)

def crear(request):
    context = {}
    return render(request, "tmp_crear.html", context)

def buscar(request):
    return render(request, "tmp_buscar.html", {})

##Clientes
def clientes(request):
    return HttpResponse("Hola!")

def clientes_crear(request):
    form = ClienteForm()
    context = {"form" : form, "tipo" : "Cliente"}

    if request.method == "POST":
        form = ClienteForm(request.POST)

        if form.is_valid:
            form.save()
    
    return render(request, 'tmp_crear_form.html', context)


def clientes_buscar(request):
    clientes_buscados = []
    dato = request.GET.get("partial", None)

    if dato is not None:
        clientes_buscados = Cliente.objects.filter(nombre__icontains = dato)
    
    buscador = Busqueda()

    return render(
        request, "tmp_buscar_cliente.html",
        {"buscador" : buscador,
        "clientes_buscados" : clientes_buscados,
        "dato" : dato} 
    )

##Proveedores

def proveedores(request):
    return HttpResponse("Hola!")

def proveedores_crear(request):
    form = ProveedorForm()
    context = {"form" : form, "tipo" : "Proveedor"}

    if request.method == 'POST':
        form = ProveedorForm(request.POST)

        if form.is_valid:
            form.save()
    
    return render(request, "tmp_crear_form.html", context)

def proveedores_buscar(request):
    proveedores_buscados = []
    dato = request.GET.get("partial", None)
    
    if dato is not None:
        proveedores_buscados = Proveedor.objects.filter(nombre__icontains = dato)
    buscador = Busqueda()

    return render(
        request, "tmp_buscar_proveedor.html",
        {"buscador" : buscador,
        "proveedores_buscados" : proveedores_buscados,
        "dato" : dato} 
    )
##Productos

def productos(request):
    return HttpResponse("Hola!")

def productos_crear(request):
    form = ProductoForm()
    context = {"form" : form, "tipo" : "Producto"}

    if request.method == 'POST':
        form = ProductoForm(request.POST)

        if form.is_valid:
            form.save()
    return render(request, "tmp_crear_form.html", context)

def productos_buscar(request):
    productos_buscados = []
    dato = request.GET.get("partial", None)
    
    if dato is not None:
        productos_buscados = Producto.objects.filter(nombre__icontains = dato)
    buscador = Busqueda()

    return render(
        request, "tmp_buscar_productos.html",
        {"buscador" : buscador,
        "productos_buscados" : productos_buscados,
        "dato" : dato} 
    )