from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Usuarios
from .forms import RegistrarUsuariosForm



class RegistrarUsuario(CreateView):
    model = Usuarios
    template_name = 'usuarios/registrar.html'
    form_class = RegistrarUsuariosForm
    success_url = reverse_lazy('index')


def ListarUsuarios(request):
    usuarios = Usuarios.objects.all()
    template_name = 'usuarios/listar_usuarios.html'
    contexto = {
        "usuarios": usuarios
    }
    return render(request, template_name, contexto)


class EliminarUsuario(LoginRequiredMixin, DeleteView):
    model = Usuarios
    template_name = 'usuarios/confirma_eliminar.html'
    success_url = reverse_lazy('apps.usuarios:listar_usuarios')



