from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    celular = models.BigIntegerField(default=0)
    edad = models.IntegerField()
    cedula = models.IntegerField()
    direccion = models.CharField(max_length=50)
    deuda = models.IntegerField()

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    celular = models.BigIntegerField(default=0)
    razon_social = models.CharField(max_length=50)
    rut = models.IntegerField()
    direccion = models.CharField(max_length=50)
    dias_visita = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio_de_venta = models.IntegerField()

    def __str__(self):
        return self.nombre