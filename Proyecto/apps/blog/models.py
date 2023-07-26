from django.db import models
from django.utils import timezone
from apps.usuarios.models import Usuarios



class Categorias(models.Model):
    nombre = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    category = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)
    titulo = models.CharField(max_length=255, null=False)
    texto = models.TextField(null=False)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    colaborador = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True, default=1)
    imagen = models.ImageField(null=True, blank=True, upload_to='blog', default="blog/imagen_default.png")
    published = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ('-published',)


""" 
#Consultar: Si esta class se puede desarrollar en la app blog;

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()   
    telefono = models.CharField(max_length=100)



 """