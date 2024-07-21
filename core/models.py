from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

    def get_total_precio(self):
        return self.cantidad * self.producto.precio
