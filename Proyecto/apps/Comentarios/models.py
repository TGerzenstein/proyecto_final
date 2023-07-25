from django.db import models
from apps.usuarios.models import Usuarios
from apps.blog.models import Post


class Comentarios(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    texto = models.TextField(verbose_name='Comentarios')
    fecha = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto

    class Meta:
        ordering = ['-fecha']