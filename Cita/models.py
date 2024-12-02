from django.db import models
from Oftalmologos.models import Oftalmologo
from Clientes.models import Paciente

# Create your models here.
class Cita(models.Model):
    
    hora_cita = models.TimeField()
    fecha_cita = models.DateField()
    oftalmologo = models.ForeignKey(Oftalmologo, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Fecha de cita: {self.fecha_cita}\nHora Cita{self.hora_cita}.\nPaciente {self.paciente}\nOftalmologo{self.oftalmologo} "