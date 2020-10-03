from rest_framework import serializers
from .models import Solicitud

#from django.contrib.auth.models import User


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = [
        	
            'persona',
            'numero_productos',
            'detalle',
    
        ]