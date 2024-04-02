from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.forms import CrearUsuario, EditarPerfil, DatosExtrasUpdateForm

def login(request):
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contrasenia)
            django_login(request, user)
            
            return redirect('inicio')
            
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    formulario = CrearUsuario()
    
    if request.method == 'POST':
        formulario = CrearUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

def perfil(request):
    return render(request, 'usuarios/perfil.html')

def editar_perfil(request):
    
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, instance=request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect('perfil')
    else:
        formulario = EditarPerfil(instance=request.user)
    
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class EditarContrasenia(PasswordChangeView):
    template_name = "usuarios/cambiar_contrasenia.html"
    success_url = reverse_lazy('perfil')


def update_datos_extras(request):
    if request.method == 'POST':
        form = DatosExtrasUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('Datos Extras') 
    else:
        form = DatosExtrasUpdateForm(instance=request.user.profile)
    return render(request, 'editar_perfil.html', {'form': form})