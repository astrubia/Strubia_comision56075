from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from servicio.models import turno

class turnos(ListView):
    model = turno
    context_object_name = 'turnos'
    template_name = 'turnos/turnos.html'

class crear_turno(CreateView):
    model = turno
    template_name = 'turnos/crear_turno.html'
    fields = ['tipo', 'requerimiento', 'fecha_turno', 'descripcion']
    success_url = reverse_lazy('turnos')
    
class Eliminar_turno(LoginRequiredMixin, DeleteView):
    model = turno
    template_name = 'turnos/eliminar_turno.html'
    success_url = reverse_lazy('turnos')

class Editar_turno(LoginRequiredMixin, UpdateView):
    model = turno
    template_name = 'turnos/editar_turno.html'
    fields = ['tipo', 'requerimiento', 'fecha_turno', 'descripcion']
    success_url = reverse_lazy('turnos')
    
class Detalle_turno(DetailView):
    model = turno
    template_name = 'turnos/detalle_turno.html'