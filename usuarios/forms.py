from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CrearUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='repetir contrasenia', widget=forms.PasswordInput)


    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {llave:'' for llave in fields}


class EditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label="editar email")
    first_name = forms.CharField(label="nombre")
    last_name = forms.CharField(label="apellido")
    avatar = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','avatar']

