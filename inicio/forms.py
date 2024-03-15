from django import forms

class FormularioBasePaciente(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    insulinoterapia= forms.BooleanField()
    
class FormularioAltaPaciente(FormularioBasePaciente):
    pass
class FormularioEditarPaciente(FormularioBasePaciente):
    glucemia = forms.IntegerField()
    
class BusquedaPaciente(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)