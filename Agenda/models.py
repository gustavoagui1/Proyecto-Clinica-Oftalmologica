from django.db import models
from Oftalmologos.models import Oftalmologo

# Create your models here.
class Agenda(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    oftalmologo = models.ForeignKey(Oftalmologo, on_delete=models.CASCADE)

    def __str__(self):
        return f'Fecha: {self.fecha} - 
        Hora: {self.hora} - 
        Oftalmologo: {self.oftalmologo.nombre_doctor} {self.oftalmologo.apellido_doctor}'