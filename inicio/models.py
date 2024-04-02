from django.db import models
from ckeditor.fields import RichTextField

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    glucemia = models.IntegerField()
    insulinoterapia = models.BooleanField(default=False)
    descripcion = RichTextField(null=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad} - {self.glucemia} - {self.insulinoterapia}"
    
class eliminar_paciente(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    glucemia = models.IntegerField()
    insulinoterapia = models.BooleanField(default=False)