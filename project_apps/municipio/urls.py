from django.urls import path
from project_apps.municipio.views import getMunicipio, getMunicipios, getRoutes

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('Municipios/', getMunicipios, name= 'Municipio'),
    path('Municipio/<int:pk>/', getMunicipio, name="Municipio")
]