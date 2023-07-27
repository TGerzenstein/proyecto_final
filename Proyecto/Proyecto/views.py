from django.shortcuts import render


def index(request):
    template_name = 'index.html'
    return render(request, template_name) 

def contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')