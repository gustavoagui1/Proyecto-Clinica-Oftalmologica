from django.db import models

# Create your models here.
class Receta(models.Model):
    receta = models.CharField(max_length=300)
    paciente = models.IntegerField()
    oftalmologo = models.IntegerField()
