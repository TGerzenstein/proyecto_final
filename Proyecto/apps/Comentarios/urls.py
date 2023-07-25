from django.urls import path
from .views import AgregarComentario, ModificarComentario, EliminarComentario

app_name = 'apps.Comentarios'

urlpatterns = [
    path('agregar_Comentario/', AgregarComentario, name='agregar_Comentario'),
    path("modificarComentario/<int:pk>",
         ModificarComenrario.as_view(), name='modificarComentario'),
    path("eliminar_opinion/<int:pk>",
         EliminarComentrario.as_view(), name='eliminarComentario'),
]


