"""
URL configuration for prueba_3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from prueba_3_app.views import RenderSeminario, instituciones, Agregar, RenderIndex, Usuario, ListadoSeminario, ListadoInstituciones, buscar_id, DetalleView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', RenderIndex),
    path('listado/', RenderSeminario, name='RenderSeminario'),
    path('agregar/', Agregar, name='Agregar'),
    path('instituciones/', instituciones, name='instituciones'),
    path('usuario', Usuario),
    path('buscar/', buscar_id, name='buscar_id'),
    path('detalle/<int:pk>/', DetalleView.as_view(), name='detalle_api'),

    path('seminarioclass', ListadoSeminario.as_view()),
    path('institucionclass', ListadoInstituciones.as_view()),
    
]