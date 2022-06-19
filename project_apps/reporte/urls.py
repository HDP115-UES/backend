from django.urls import path
from project_apps.reporte.views import getReporte,getReportes, getRoutes

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('Reportes/', getReportes, name= 'Reportes'),
    path('Reporte/<int:pk>/', getReporte, name="Reporte")
]