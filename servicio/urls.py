from django.urls import path
from servicio import views

urlpatterns = [
    path('turnos/', views.turnos.as_view(), name='turnos'),
    path('turnos/crear_turno', views.crear_turno.as_view(), name='crear_turno'),
    path('turnos/<int:pk>/', views.Detalle_turno.as_view(), name='Detalle_turno'),
    path('turnos/<int:pk>/editar/', views.Editar_turno.as_view(), name='Editar_turno'),
    path('turnos/<int:pk>/eliminar/', views.Eliminar_turno.as_view(), name='Eliminar_turno'),
]
