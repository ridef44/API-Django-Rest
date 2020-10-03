from rest_framework import serializers
from api.models import Persona

#from django.contrib.auth.models import User


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = [
            'id',
            'nombre',
            'apellido',
            'telefono',
            'email',
        ]

