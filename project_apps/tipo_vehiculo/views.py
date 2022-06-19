from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from project_apps.tipo_vehiculo.utils import getTipoVehiculosDetails, getTipoVehiculosList, createTipoVehiculo, updateTipoVehiculo, deleteTipoVehiculos

# Create your views here.

# Rutas
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/TipoVehiculos/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of TipoVehiculos'
        },
        {
            'Endpoint': '/TipoVehiculo/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single TipoVehiculos object'
        },
        {
            'Endpoint': '/TipoVehiculos/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new TipoVehiculos with data sent in post request'
        },
        {
            'Endpoint': '/TipoVehiculo/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing TipoVehiculos with data sent in post request'
        },
        {
            'Endpoint': '/TipoVehiculo/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting TipoVehiculos'
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getTipoVehiculos(request):
    if request.method == 'GET':
        return getTipoVehiculosList(request)
    elif request.method == 'POST':
        return createTipoVehiculo(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getTipoVehiculo(request, pk):
    if request.method == 'GET':
        return getTipoVehiculosDetails(request, pk)
    elif request.method == 'PUT':
        return updateTipoVehiculo(request, pk)
    elif request.method == 'DELETE':
        return deleteTipoVehiculos(request, pk)