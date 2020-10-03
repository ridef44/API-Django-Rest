from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from api.views import Login, Logout



from api.views import Homepage


urlpatterns = [
    
    #Rutas de API'S
    path('api/', include(('api.urls', 'api'))),
    path('api_generate_token/', views.obtain_auth_token),


    #Ruta para el administrador DJANGO
    path('admin/', admin.site.urls),

    #Url's para pagina de Inicio
    path('homepage/', Homepage.as_view(), name='homepage'),



    #Vistas con Templates
    path('producto/', include('apps.producto.urls', namespace='producto')),
    path('venta/', include('apps.venta.urls', namespace='venta')),


    #Rutas para Ingreso, Registro y salida
    #Pagina de inicio: http://127.0.0.1:8000/accounts/login/
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registro/', include(('api.urls', 'registro'))),
    


]
