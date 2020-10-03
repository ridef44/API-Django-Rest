from django.urls import path, include
from apps.venta.views import SolcitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

#Importar la vista para visualizar API
from apps.venta.views import SolcitudListApi

from django.contrib.auth.decorators import login_required

app_name = 'apps'

urlpatterns = [

#Rutas para visializar API's


    path('solicitudApi', login_required(SolcitudListApi.as_view()), name='api_solicitud'),

 #Rutas para obiones de Operaciones 
   
    path('listar', login_required(SolcitudList.as_view()), name='solicitud_listar'),
    path('nueva', login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
    path('editar/<int:pk>/',login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
    path('eliminar/<int:pk>/', login_required(SolicitudDelete.as_view()),
         name='solicitud_eliminar'),


]
