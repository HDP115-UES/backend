from django.urls import path
from project_apps.tipo_accidente.views import getTipoAccidente, getTipoAccidentes, getRoutes

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('TipoAccidentes/', getTipoAccidentes, name= 'TipoAccidente'),
    path('TipoAccidente/<int:pk>/', getTipoAccidente, name="TipoAccidenteDetail")
]