from rest_framework import serializers
from .models import Producto, Pago

#from django.contrib.auth.models import User


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'precio',
            'fecha_venta',
            'descripcion',
            'persona',
            'pago'
        ]

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = [
            'id',
            'nombre',
        ]


