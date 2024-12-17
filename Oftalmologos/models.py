from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Oftalmologo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_doctor = models.CharField(max_length=30)
    apellido_doctor = models.CharField(max_length=30)
    rut_doctor = models.CharField(max_length=9)

    def __str__(self):
        return f"Nombre Doctor: {self.nombre_doctor} {self.apellido_doctor}"
    