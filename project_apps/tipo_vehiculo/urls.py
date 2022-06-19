from django.urls import path
from project_apps.tipo_vehiculo.views import getRoutes, getTipoVehiculo, getTipoVehiculos

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('TipoVehiculos/', getTipoVehiculos, name= 'TipoVehiculos'),
    path('TipoVehiculo/<int:pk>/', getTipoVehiculo, name="TipoVehiculoDetail")
]