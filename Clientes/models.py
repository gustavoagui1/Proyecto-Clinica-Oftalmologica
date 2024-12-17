from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_paciente = models.CharField(max_length=30)
    apellido_paciente = models.CharField(max_length=30)
    rut_paciente = models.CharField(max_length=9)

    def __str__(self):
        return f"Nombre Paciente: {self.nombre_paciente} {self.apellido_paciente}"