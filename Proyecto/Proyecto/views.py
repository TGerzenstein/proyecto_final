from django.shortcuts import render


def index(request):
    return render(request, 'index.html') 

def contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')