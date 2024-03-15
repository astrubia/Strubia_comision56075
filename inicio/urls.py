from django.urls import path
from inicio.views import inicio, alta_paciente, pacientes, ver_paciente, eliminar_paciente, editar_paciente

urlpatterns = [
    path('', inicio, name='inicio'),
    path('alta_paciente/', alta_paciente, name='alta_paciente'),
    path('pacientes/', pacientes, name='pacientes'),
    path('pacientes/<int:id_paciente>', ver_paciente, name='ver_paciente'),
    path('pacientes/<int:id_paciente>/eliminar', eliminar_paciente, name='eliminar_paciente'),
    path('pacientes/<int:id_paciente>/editar', editar_paciente, name='editar_paciente'),
]
