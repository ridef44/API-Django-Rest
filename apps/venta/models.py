from django.db import models
from api.models import Persona

# Create your models here.


class Solicitud(models.Model):
    persona = models.ForeignKey(
        Persona, null=True, blank=True, on_delete=models.CASCADE)
    numero_productos = models.IntegerField()
    detalle = models.TextField()
