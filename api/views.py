
from django.views.generic import TemplateView
from rest_framework import generics
from django.shortcuts import redirect

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Proteccion de cache en navegadores
from django.views.decorators.cache import never_cache
# Proteccion Cross-site request forger
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout,  authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView


from django.contrib.auth.models import User

from django.views.generic.edit import CreateView
from apps.producto.views import ProductoList

from api.forms import RegistroForm
#from apps.usuario.serializers import UserSerializer


from .models import Persona
from .serializers import PersonaSerializer


#Vista para crear pagina de inicio
class Homepage(TemplateView):
    template_name = "home.html"


#Vista para desplegar listado de Clientes por medio de APIView
class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [IsAuthenticated]
    authentication_class = [TokenAuthentication]

#Vista para generar Login e Asignacion de Token Para visualizar las Api's
class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('homepage')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        token, _ = Token.objects.get_or_create(user=user)
        if token:
            login(self.request, form.get_user())
            return super(Login, self).form_valid(form)

#Vista para Salir
class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')

#Vista para Registrar Usuarios
class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login')

