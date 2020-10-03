from django.urls import path
from apps.producto.views import ProductoCreate, ProductoList, ProductoUpdate, ProductoDelete, PagoCreate, PagoList, PagoDelete, PagoUpdate


#Importacion para las vistas de API's
from apps.producto.views import ProductoListApi, PagoListApi

#Opcion para ver Templates solo con LOGIN
from django.contrib.auth.decorators import login_required


app_name = 'apps.producto'

urlpatterns = [

    #Rutas para tipos de Pago

    path('pago', login_required(PagoCreate.as_view()), name='pago_crear'),
    path('pago_listar', login_required(PagoList.as_view()), name='pago_listar'),
    path('pago_eliminar/<int:pk>/', login_required(PagoDelete.as_view()), name='pago_eliminar'),
    path('pago_editar/<int:pk>/', login_required(PagoUpdate.as_view()), name='pago_editar'),


    #Rutas para Api's'
    path('productoApi', login_required(ProductoListApi.as_view()), name='api_producto'),
    path('pagoApi', login_required(PagoListApi.as_view()), name='api_pago'),



    #Rutas para Productos
    path('nuevo', login_required(ProductoCreate.as_view()), name="producto_crear"),
    path('listar', login_required(ProductoList.as_view()), name='producto_listar'),
    path('editar/<int:pk>/', login_required(ProductoUpdate.as_view()), name='producto_editar'),
    path('eliminar/<int:pk>/', login_required(ProductoDelete.as_view()), name='producto_eliminar'),






]
