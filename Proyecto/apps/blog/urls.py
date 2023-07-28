from django.urls import path
from .views import AgregarCategoria, AgregarPost
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import AgregarCategoria, AgregarPost, EliminarPost, ListarPost, ListarPostPorCategoria, Post_detalle, ModificarPost, ordenar_libros_por


app_name= 'apps.blog'
  

urlpatterns = [
    path('agregar_categoria/', AgregarCategoria.as_view(),name='agregar_categoria'),
    path('agregar_post/', AgregarPost.as_view(), name='agregar_post'),
    path("modificar_post/<int:pk>",
         ModificarPost.as_view(), name='modificar_post'),
    path("eliminar_libro/<int:pk>", EliminarPost.as_view(), name='eliminar_post'),
    path("listar_post/", ListarPost.as_view(), name='listar_post'),
    path("post_detalle/<int:id>", Post_detalle, name='post_detalle'),
    path("listar_por_categoria/<str:categoria>", ListarPostPorCategoria, name='listar_por_categoria'),
    path("ordenar_por/", ordenar_libros_por, name='ordenar_por'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)