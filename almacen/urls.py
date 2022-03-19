from django.urls import path
from .views import inicio, clientes, clientes_crear, crear, proveedores, proveedores_crear, productos, productos_crear, buscar, clientes_buscar,productos_buscar,proveedores_buscar

urlpatterns = [
    path("index/", inicio, name="inicio"),
    ##Crear
    path("crear/", crear, name="crear"),

    ##Buscar
    path("buscar/", buscar, name="buscar"),

    ##Clientes
    path("clientes/", clientes, name="clientes"),
    path("clientes/crear", clientes_crear, name="clientes_crear"),
    path("clientes/buscar", clientes_buscar, name="clientes_buscar"),

    #Proveedores
    path("proveedores/", proveedores, name="proveedores"),
    path("proveedores/crear", proveedores_crear, name="proveedores_crear"),
    path("proveedores/buscar", proveedores_buscar, name="proveedores_buscar"),
    
    #Productos
    path("productos/", productos, name="productos"),
    path("productos/crear", productos_crear, name="productos_crear"),
    path("productos/buscar", productos_buscar, name="productos_buscar"),
    ]