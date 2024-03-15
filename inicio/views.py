from django.shortcuts import render, redirect
from inicio.models import Paciente
import random as ramdon
from inicio.forms import FormularioAltaPaciente, BusquedaPaciente, FormularioEditarPaciente

def inicio(request):
    return render(request, 'padre.html')

def pacientes(request):
    pacientes = Paciente.objects.all()
    formulario = BusquedaPaciente(request.GET)
    if formulario.is_valid():
        nombre = formulario.cleaned_data.get('nombre')
        if nombre:
            pacientes = Paciente.objects.filter(nombre__icontains=nombre)
    
    return render(request, 'inicio/pacientes.html', {'pacientes': pacientes, 'formulario': formulario})

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
    return render(request, 'inicio/alta_paciente.html',{"formulario": formulario})

def eliminar_paciente(request, id_paciente):
    paciente = Paciente.objects.get(id=id_paciente)
    paciente.delete()
    return redirect('pacientes')

def editar_paciente(request, id_paciente):
    paciente = Paciente.objects.get(id=id_paciente)
    formulario = FormularioEditarPaciente(initial={ "nombre": paciente.nombre, "apellido": paciente.apellido, "edad": paciente.edad, "glucemia": paciente.glucemia, "insulinoterapia": paciente.insulinoterapia})
    if request.method == 'POST':
        formulario = FormularioEditarPaciente(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            paciente.nombre = informacion.get('nombre')
            paciente.apellido = informacion.get('apellido')
            paciente.edad = informacion.get('edad')
            paciente.glucemia = informacion.get('glucemia')
            paciente.insulinoterapia = informacion.get('insulinoterapia')
            paciente.save()  
        return redirect('pacientes')
    return render(request, 'inicio/editar_paciente.html', {"paciente": paciente, "formulario": formulario})

def ver_paciente(request, id_paciente):
    paciente = Paciente.objects.get(id=id_paciente)
    return render(request, 'inicio/ver_paciente.html', {"paciente": paciente})