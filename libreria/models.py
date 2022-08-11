from ast import Delete
from turtle import title
from django.db import models

# Create your models here.
class Libro(models.Model):
    id= models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=100, verbose_name= 'Titulo')
    Imagen = models.ImageField(upload_to='imagenes/', verbose_name="Imagen", null=True)
    Autor = models.CharField(max_length=100)
    Genero = models.CharField(max_length=100)
    Año =  models.CharField(max_length=100)
    Descripcion = models.TextField(verbose_name= "Descripcion", null=True)
    Editorial = models.CharField(max_length=100)
    def __str__(self):
      fila = "Titulo: " + self.Titulo + " - " + " Descripcion: " + self.Descripcion + " Editorial: " + self.Editorial
      return fila
    
    def delete(self, using=None, keep_parents=False):
        self.Imagen.storage.delete(self.imagen.name)
        super().delete()