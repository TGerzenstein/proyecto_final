from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Categorias, Post
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

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


