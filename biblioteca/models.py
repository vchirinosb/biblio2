from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=450, blank=True, null=True)
    
    class Meta:
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class Editorial(models.Model):
    editorial = models.CharField(max_length=150)
    
    class Meta:
        ordering = ['editorial']
    
    def __str__(self):
        return self.editorial

class Libro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT)
    titulo = models.CharField(max_length=250)
    anhopublicacion = models.IntegerField()
    edicion = models.CharField(max_length=20)
    imagenportada = models.ImageField(blank=True, null=True)
    cantidadejemplares = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['titulo', 'autor', 'editorial']
    
    def __str__(self):
        return self.titulo
