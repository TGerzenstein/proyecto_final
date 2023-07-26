from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Categorias, Post
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from typing import Any, Dict
from django.db.models.query import QuerySet
# Create your views here.


class AgregarCategoria(LoginRequiredMixin, CreateView):
    model = Categorias
    fields = ['nombre']
    template_name = 'blog/agregar_categoria.html'
    success_url = reverse_lazy('index')


class AgregarPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['category','titulo','texto','imagen']
    template_name = 'blog/agregar_post.html'
    success_url = reverse_lazy('index')


class ModificarPost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titulo', 'colaborador', 'texto', 'imagen', 'category']
    template_name = 'blog/agregar_post.html'
    success_url = reverse_lazy('apps.blog:listar_post')


class EliminarPost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/confirma_eliminar.html'
    success_url = reverse_lazy('apps.blog:listar_post')


class ListarPost(ListView):
    model = Post
    template_name = 'blog/listar_post.html'
    context_object_name = "post"
    # -----Paginación------
    paginate_by = 3

    def get_context_data(self):
        context = super().get_context_data()
        categorias = Categorias.objects.all()
        context['category'] = categorias
        return context

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)
        return queryset.order_by('titulo')


def ListarLibrosPorCategoria(request, categoria):
    categorias2 = Categorias.objects.filter(nombre=categoria)
    post = Post.objects.filter(
        categoria=categorias2[0].id).order_by('fecha_agregado')
    categorias = Categorias.objects.all()
    template_name = 'libros/listar_libros.html'
    contexto = {
        'libros': post,
        'categorias': categorias
    }
    return render(request, template_name, contexto)