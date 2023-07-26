from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import RegistrarUsuario


app_name = 'apps.usuarios'

urlpatterns = [
    path("registrar/", RegistrarUsuario.as_view(), name='registrar'),
    path('iniciar_sesion/', LoginView.as_view(
        template_name="usuarios/iniciar_sesion.html"), name='iniciar_sesion'),
    path('cerrar_sesion/',LogoutView.as_view(
        template_name="usuarios/cerrar_sesion.html"), name='cerrar_sesion'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)