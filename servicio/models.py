from django.db import models
from ckeditor.fields import RichTextField

class turno(models.Model):
    tipo = models.CharField(max_length=50)
    requerimiento = models.CharField(max_length=50)
    fecha_turno = models.DateField()
    descripcion = RichTextField(null=True)

    def __str__(self):
        return f"{self.tipo} {self.requerimiento}"