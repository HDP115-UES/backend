from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from project_apps.tipo_accidente.utils import getTipoAccidentesDetails, getTipoAccidentesList, createTipoAccidente, updateTipoAccidente, deleteTipoAccidente

# Create your views here.

# Rutas
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/TipoAccidentes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of TipoAccidentes'
        },
        {
            'Endpoint': '/TipoAccidente/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single TipoAccidentes object'
        },
        {
            'Endpoint': '/TipoAccidentes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new TipoAccidentes with data sent in post request'
        },
        {
            'Endpoint': '/TipoAccidente/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing TipoAccidentes with data sent in post request'
        },
        {
            'Endpoint': '/TipoAccidente/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting TipoAccidentes'
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getTipoAccidentes(request):
    if request.method == 'GET':
        return getTipoAccidentesList(request)
    elif request.method == 'POST':
        return createTipoAccidente(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getTipoAccidente(request, pk):
    if request.method == 'GET':
        return getTipoAccidentesDetails(request, pk)
    elif request.method == 'PUT':
        return updateTipoAccidente(request, pk)
    elif request.method == 'DELETE':
        return deleteTipoAccidente(request, pk)
        