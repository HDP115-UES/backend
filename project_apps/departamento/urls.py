from django.urls import path
from project_apps.departamento.views import getDepartamento, getDepartamentos, getRoutes
urlpatterns = [
    path('', getRoutes, name="routes"),
    path('Departamentos/', getDepartamentos, name= 'Departamentos'),
    path('Departamento/<int:pk>/', getDepartamento, name="DepartamentoDetail")
]