from django.db import models
#from django.contrib.auth.models import Usuarios #Usuario que publicará el artículo
from django.utils import timezone



class Categorias(models.Model):
    nombre = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nombre


class Post(models.Model):
    category = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)
    titulo = models.CharField(max_length=255, null=False)
    texto = models.TextField(null=False)
    fecha_agregado = models.DateTimeField(date_now_add=True)
    colaborador = models.ForeignKey(Usuarios, on_delete=models.CASCADE, null=False)
    imagen = models.ImageField(null=True, blank=True, upload_to='media')
    published = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ('-published',)




