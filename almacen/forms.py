from django import forms

from almacen.models import Cliente, Producto, Proveedor


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = "__all__"

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

class Busqueda(forms.Form):
    #opciones = ("Clientes", "Productos", "Proveedores")

    partial = forms.CharField(label="Buscador", max_length=50)
    #opcion = forms.CharField(choices=opciones)
