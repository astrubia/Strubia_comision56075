from django.urls import path
from inicio.views import inicio, alta_paciente, pacientes

urlpatterns = [
    path('', inicio, name='inicio'),
    path('alta_paciente/', alta_paciente, name='alta_paciente'),
    path('pacientes/', pacientes, name='pacientes'),
]
