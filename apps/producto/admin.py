from django.contrib import admin
from apps.producto.models import Pago, Producto

# Register your models here.
admin.site.register(Pago)
admin.site.register(Producto)
