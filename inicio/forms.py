from django import forms
from ckeditor.fields import RichTextFormField

class FormularioBasePaciente(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    insulinoterapia= forms.BooleanField()
    descripcion = RichTextFormField()
    imagen = forms.ImageField()
    
class FormularioAltaPaciente(FormularioBasePaciente):
    pass
class FormularioEditarPaciente(FormularioBasePaciente):
    glucemia = forms.IntegerField()
    
class BusquedaPaciente(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)