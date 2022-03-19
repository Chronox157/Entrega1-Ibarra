from django.contrib import admin
from .models import Cliente, Proveedor, Producto

# Register your models here.

class postAdmin(admin.ModelAdmin):
    admin.site.register(Cliente)
    admin.site.register(Proveedor)
    admin.site.register(Producto)
