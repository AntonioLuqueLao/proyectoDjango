from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Seccion(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    imagen=models.ImageField(upload_to="tienda", null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    secciones=models.ForeignKey(Seccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre