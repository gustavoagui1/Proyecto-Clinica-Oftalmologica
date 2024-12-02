from django.db import models
from Oftalmologos.models import Oftalmologo 
from Clientes.models import Paciente

# Create your models here.
class Receta(models.Model):
    receta = models.CharField(max_length=300)
    paciente = models.IntegerField()
    oftalmologo = models.ForeignKey(Oftalmologo, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Receta de {self.paciente} por {self.oftalmologo}"
