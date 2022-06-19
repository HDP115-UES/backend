from django.urls import path
from project_apps.registro.views import getRegistro, getRegistros, getRoutes

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('Registros/', getRegistros, name= 'Registros'),
    path('Registro/<int:pk>/', getRegistro, name="Registro")
]