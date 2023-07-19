from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *

# Create your views here.


class AgregarCategoria(CreateView):
    model = Categorias
    fields = ['nombre']
    template_name = 'blog/agregar_categoria.html'
    success_url = reverse_lazy('index')


class AgregarPost(CreateView):
    model = Post
    fields = ['category','titulo','texto','imagen']
    template_name = 'blog/agregar_post.html'
    success_url = reverse_lazy('index')