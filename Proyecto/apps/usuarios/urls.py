from django.contrib import admin
from django.urls import path, include
from .views import RegistrarUsuario



urlpatterns = [
    path("registrar/", RegistrarUsuario.as_view(), name='registrar'),
]