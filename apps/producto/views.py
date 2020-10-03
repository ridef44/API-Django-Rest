from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import generics

#Import de Serializers
from .serializers import ProductoSerializer, PagoSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from apps.producto.forms import ProductoForm, PagoForm
from apps.producto.models import Producto, Pago



#Vistas para Gestionarlas desde APIView
class ProductoListApi(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]
    authentication_class = [TokenAuthentication]

class PagoListApi(generics.ListCreateAPIView):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [IsAuthenticated]
    authentication_class = [TokenAuthentication]



#Vistas para crear Productos y Tipos de Pago
class ProductoCreate(CreateView):
    model = Producto
    #fields = '__all__'
    form_class = ProductoForm
    template_name = 'producto/pago_create.html'
    success_url = reverse_lazy('producto:producto_listar')

class PagoCreate(CreateView):
    model = Pago
    #fields = '__all__'
    form_class = PagoForm
    template_name = 'producto/producto_form.html'
    success_url = reverse_lazy('producto:pago_listar')

#Vistas para Listar Productos y Tipos de pago
class ProductoList(ListView):
    model = Producto
    template_name = 'producto/producto_list.html'
    ordering = ['id']

class PagoList(ListView):
    model = Pago
    template_name = 'producto/pago_list.html'
    ordering = ['id']




#Vistas para Modificar Productos y Tipos de Pago
class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto_form.html'

    def get_success_url(self):
        return reverse('producto:producto_listar')


class PagoUpdate(UpdateView):
    model = Pago
    form_class = PagoForm
    template_name = 'producto/pago_create.html'

    def get_success_url(self):
        return reverse('producto:pago_listar')

#Vistas para Borrar Productos y Tipos de Pago
class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'producto/producto_delete.html'
    success_url = reverse_lazy('producto:producto_listar')

class PagoDelete(DeleteView):
    model = Pago
    template_name = 'producto/pago_delete.html'
    success_url = reverse_lazy('producto:pago_listar')
