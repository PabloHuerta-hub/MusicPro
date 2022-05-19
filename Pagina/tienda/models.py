import email
from mailbox import NoSuchMailboxError
from pyexpat import model
from tkinter import CASCADE
from django.utils import timezone
from django.db import models

# Create your models here.
class Tipo_Instrumento(models.Model) :
    nombre = models.CharField(max_length=30)

    def __str__(self) :
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_instrumento = models.ForeignKey(Tipo_Instrumento, on_delete= models.CASCADE)
    
    def __str__(self) :
        return self.nombre

class SubCategoria(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)
    
    def __str__(self) :
        return self.nombre

class Producto(models.Model) :
    serie_producto = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    codigo = models.CharField(max_length=15)
    marca = models.CharField(max_length=30)
    precio = models.IntegerField()
    sub_categoria = models.ForeignKey(SubCategoria, on_delete= models.CASCADE)
    #created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return self.nombre