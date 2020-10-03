from django import forms
from apps.producto.models import Producto, Pago


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto

        fields = ['nombre', 'precio', 'fecha_venta',
                  'descripcion', 'persona', 'pago', ]

        labels = [{
            'nombre': 'Nombre',
            'precio': 'Precio',
            'fecha_venta': 'Fecha De Venta',
            'descripcion': 'Descripcion',
            'persona': 'Persona Compro',
            'pago': 'Tipo de Pago',
        }
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_venta': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'pago': forms.CheckboxSelectMultiple(),

        }

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago

        fields = ['nombre']
        labels = [{'nombre': 'Nombre'}]
        widgets = {'nombre': forms.TextInput(attrs={'class': 'form-control'})}