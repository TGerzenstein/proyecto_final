from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from .forms import ComentariosForm
from .models import Comentarios


#Views

def AgregarComentario(request):
    form = ComentariosForm(request.POST or None)
    if form.is_valid():
        form.save()

    contexto = {
        'form': form,
    }
    template_name = 'comentarios/agregar_comentario.html'
    return render(request, template_name, contexto)


class ModificarComentario(LoginRequiredMixin, UpdateView):
    model = Comentarios
    fields = ['texto']
    template_name = 'comentarios/agregar_comentario.html'
    success_url = reverse_lazy('apps.post:listar_post')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(usuario = self.request.user)


class EliminarComentario(LoginRequiredMixin, DeleteView):
    model = Comentarios
    template_name = 'post/confirma_eliminar.html'
    success_url = reverse_lazy("apps.post:listar_post")