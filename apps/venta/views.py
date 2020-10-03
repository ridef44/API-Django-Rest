from rest_framework import generics
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

#Importar permisos para autenticar por medio de Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

#Importar los serializers
from apps.venta.serializers import SolicitudSerializer

from apps.venta.models import Solicitud
from apps.venta.forms import SolicitudForm, PersonaForm
from api.models import Persona



#Vistas para visualizar las API's de Las Operaciones realizadas
class SolcitudListApi(generics.ListCreateAPIView):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer
    permission_classes = [IsAuthenticated]
    authentication_class = [TokenAuthentication]


#Listar las ventas
class SolcitudList(ListView):
    model = Solicitud
    template_name = 'venta/venta_list.html'

#Vista para crear y asignar un producto a un Cliente
class SolicitudCreate(CreateView):
    model = Solicitud
    template_name = 'venta/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('venta:solicitud_listar')

    def get_context_data(self, **kwargs):
        context = super(SolicitudCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
            return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = form2.save()
            solicitud.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

#Vista para poder modificar los registros realizados
class SolicitudUpdate(UpdateView):
    model = Solicitud
    second_model = Persona
    template_name = 'venta/solicitud_form.html'
    form_class = SolicitudForm
    second_form_class = PersonaForm
    success_url = reverse_lazy('venta:solicitud_listar')

    def get_context_data(self, **kwargs):
        context = super(SolicitudUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        solicitud = self.model.objects.get(id=pk)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=persona)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_solicitud = kwargs['pk']
        solicitud = self.model.objects.get(id=id_solicitud)
        persona = self.second_model.objects.get(id=solicitud.persona_id)
        form = self.form_class(request.POST, instance=solicitud)
        form2 = self.second_form_class(request.POST, instance=persona)

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

#Eliminar las ventas hechas.

class SolicitudDelete(DeleteView):
    model = Solicitud
    template_name = 'venta/solicitud_delete.html'
    success_url = reverse_lazy('venta:solicitud_listar')


