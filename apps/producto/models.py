from django.db import models
from api.models import Persona


class Pago(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)


# nos crea los modelos, primero makemigrations para hacer las migraciones luego migrate para crear tablas
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_venta = models.DateField()
    descripcion = models.TextField(blank=True)
    # Nos crea la relacion de uno a uno con la tabla persona
    persona = models.ForeignKey(
        Persona, null=True, blank=True, on_delete=models.CASCADE)
    pago = models.ManyToManyField(Pago, blank=True)
