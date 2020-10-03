from django import forms

from apps.venta.models import Solicitud
from api.models import Persona


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = [
            'nombre',
            'apellido',
            'telefono',
            'email',

        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellidos',
            'telefono': 'Teléfono',
            'email': 'Correo electrónico',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

        }


class SolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = [
            'numero_productos',
            'detalle',
        ]
        labels = {
            'numero_productos': 'Numero de Productos',
            'detalle': 'Detalle de Venta',

        }
        widgets = {
            'numero_productos': forms.TextInput(attrs={'class': 'form-control'}),
            'detalle': forms.Textarea(attrs={'class': 'form-control'}),
        }
