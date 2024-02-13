from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    dicc = {
        'nombre': 'Cristian',
        'apellido': 'Perez',
    }
    
    return render(request, 'inicio.html', dicc)
