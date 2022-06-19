from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from project_apps.accidente.utils import getAccidenteDetails, getAccidentesList, updateAccidente, deleteAccidente, createAccidente

# Create your views here.

# Rutas
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/Accidentes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of Accidentes'
        },
        {
            'Endpoint': '/Accidente/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single Accidentes object'
        },
        {
            'Endpoint': '/Accidente/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new Accidentes with data sent in post request'
        },
        {
            'Endpoint': '/Accidente/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing Accidentes with data sent in post request'
        },
        {
            'Endpoint': '/Accidente/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting Accidentes'
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getAccidentes(request):
    if request.method == 'GET':
        return getAccidentesList(request)
    elif request.method == 'POST':
        return createAccidente(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getAccidente(request, pk):
    if request.method == 'GET':
        return getAccidenteDetails(request, pk)
    elif request.method == 'PUT':
        return updateAccidente(request, pk)
    elif request.method == 'DELETE':
        return deleteAccidente(request, pk)
        