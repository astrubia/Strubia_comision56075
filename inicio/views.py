from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Paciente
import random as ramdon
from inicio.forms import FormularioAltaPaciente

def inicio(request):
    return render(request, 'inicio.html')

def pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes.html', {'pacientes': pacientes})

def alta_paciente(request):
    formulario = FormularioAltaPaciente()
    if request.method == 'POST':
        formulario = FormularioAltaPaciente(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            apellido = formulario.cleaned_data.get('apellido')
            edad = formulario.cleaned_data.get('edad')
            glucemia = ramdon.randint(50, 400)
            insulinoterapia = formulario.cleaned_data.get('insulinoterapia')
        
    
            paciente = Paciente(nombre=nombre, apellido=apellido, edad=edad, glucemia=glucemia, insulinoterapia=insulinoterapia)
            paciente.save()
        return redirect('pacientes')
    return render(request, 'alta_paciente.html',{"formulario": formulario})