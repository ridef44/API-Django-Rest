from django.db import models


# Modelo para crear las migraciones


class Persona(models.Model):
   # id = models.AutoField(primary_key=True) Django asigna ID tipo autoincremental. que es la llave primaria
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=70)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    # domicilio= models.TextField()

    # Vista por defecto para cada instancia del modelo persona
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
