from django.contrib import admin
from .models import Post, Categorias

# Register your models here.

admin.site.register(Categorias)
admin.site.register(Post)
