from django.db import models

# Create your models here.
class Oftalmologo(models.Model):
    nombre_doctor = models.CharField(max_length=30)
    apellido_doctor = models.CharField(max_length=30)
    rut_doctor = models.CharField(max_length=9)

    def __str__(self):
        return f"Nombre Doctor: {self.nombre_doctor} {self.apellido_doctor}"
    