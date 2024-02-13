from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    glucemia = models.IntegerField()
    insulinoterapia = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad} - {self.glucemia} - {self.insulinoterapia}"