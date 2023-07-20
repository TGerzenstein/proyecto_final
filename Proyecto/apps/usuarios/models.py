from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Usuarios(AbstractUser):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField('Fecha_nacimiento', default='2000-1-1')
    es_colaborador = models.BooleanField('Es_colaborador', default=False)
    imagen = models.ImageField(null=True, blank=True, upload_to='usuarios', default='usuarios/img_defecto.png')


    def __str__(self):
        return self.nombre

