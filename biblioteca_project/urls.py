from django.contrib import admin
from django.urls import path, include, re_path
from libros.soap_services import django_soap_application
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='home'),
    
    # Páginas de ejemplos
    path('ejemplos/rest/', views.ejemplos_rest, name='ejemplos_rest'),
    path('ejemplos/soap/', views.ejemplos_soap, name='ejemplos_soap'),
    path('ejemplos/admin/', views.ejemplos_admin, name='ejemplos_admin'),
    
    # Admin
    path('admin/', admin.site.urls),
    
    # Servicio SOAP
    re_path(r'^soap/', django_soap_application),
    
    # API REST
    path('api/', include('libros.urls')),
]