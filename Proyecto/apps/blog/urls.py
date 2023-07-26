from django.urls import path
from .views import AgregarCategoria, AgregarPost
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *


app_name= 'apps.blog'


urlpatterns = [
    path('agregar_categoria/', AgregarCategoria.as_view(),name='agregar_categoria'),
    path('agregar_post/', AgregarPost.as_view(), name='agregar_post'),
    #path("modificar_post/<int:pk>",
    #     ModificarPost.as_view(), name='modificar_libro'),
    path("eliminar_libro/<int:pk>", EliminarPost.as_view(), name='eliminar_post'),
    path("listar_post/", ListarPost.as_view(), name='listar_post'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)