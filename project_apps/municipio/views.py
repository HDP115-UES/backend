from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from project_apps.municipio.utils import getMunicipioDetails, getMunicipiosList, deleteMunicipio, createMunicipio, updateMunicipio

# Create your views here.

# Rutas
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/Municipios/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of Municipios'
        },
        {
            'Endpoint': '/Municipio/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single Municipios object'
        },
        {
            'Endpoint': '/Municipio/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new Municipios with data sent in post request'
        },
        {
            'Endpoint': '/Municipio/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing Municipios with data sent in post request'
        },
        {
            'Endpoint': '/Municipio/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting Municipios'
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getMunicipios(request):
    if request.method == 'GET':
        return getMunicipiosList(request)
    elif request.method == 'POST':
        return createMunicipio(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getMunicipio(request, pk):
    if request.method == 'GET':
        return getMunicipioDetails(request, pk)
    elif request.method == 'PUT':
        return updateMunicipio(request, pk)
    elif request.method == 'DELETE':
        return deleteMunicipio(request, pk)
   