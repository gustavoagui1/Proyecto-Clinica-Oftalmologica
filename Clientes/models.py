from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre_paciente = models.CharField(max_length=30)
    apellido_paciente = models.CharField(max_length=30)
    rut_paciente = models.CharField(max_length=9)

    def __str__(self):
        return f"Nombre Paciente: {self.nombre_paciente} {self.apellido_paciente}"