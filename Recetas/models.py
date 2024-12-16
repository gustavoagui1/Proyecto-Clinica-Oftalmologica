from django.db import models
from Clientes.models import Paciente

# Create your models here.
class Receta(models.Model):
    receta = models.CharField(max_length=300)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Receta de {self.paciente}"
