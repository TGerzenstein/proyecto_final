from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Categorias, Post
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from typing import Any, Dict
from django.db.models.query import QuerySet

from apps.Comentarios.models import Comentarios
from apps.Comentarios.forms import ComentariosForm

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


    def form_valid(self, form):
        form.instance.colaborador = self.request.user 
        return super().form_valid(form)



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
        context['categorias'] = categorias
        return context

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(titulo__icontains=query)
        return queryset.order_by('titulo')



def ListarPostPorCategoria(request, categoria):
    categorias2 = Categorias.objects.filter(nombre = categoria)
    post = Post.objects.filter(categoria = categorias2[0].id).order_by('fecha_agregado')
    categorias = Categorias.objects.all()
    template_name = 'blog/listar_post.html'
    contexto = {
        'post': post,
        'categorias': categorias
    }
    
    return render(request, template_name, contexto)



def Post_detalle(request, id):
    post = Post.objects.get(id=id)
    comentarios = Comentarios.objects.filter(post=id)
    form = ComentariosForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.post = post
            aux.usuario = request.user
            aux.save()
            form = ComentariosForm()
        else:
            return redirect('apps.usuarios:iniciar_sesion')

    contexto = {
        'post': post,
        'form': form,
        'comentarios': comentarios,
    }

    template_name = 'blog/post.html'
    return render(request, template_name, contexto)



def ordenar_libros_por(request):
    orden = request.GET.get('orden', '')
    if orden == 'fecha':
        post = Post.objects.order_by('fecha_agregado')
    elif orden == 'titulo':
        post = Post.objects.order_by('titulo')
    else: 
        post = Post.objects.all()

    context = {
        'post': post,
    }
    return render(request, 'blog/listar_post.html', context)
