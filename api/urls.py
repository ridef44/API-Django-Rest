from django.urls import path, include
from .views import PersonaList
from api.views import RegistroUsuario


urlpatterns = [
#Ruta para visualizar por medio de APIView
    path('persona', PersonaList.as_view(), name='persona_list'),

 #Ruta para el registro de usuarios
    path('registrar', RegistroUsuario.as_view(), name='registrar'),
]
