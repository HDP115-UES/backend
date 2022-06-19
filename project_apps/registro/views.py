from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from project_apps.registro.utils import getRegistroDetails, getRegistrosList, updateRegistro, deleteRegistro, createRegistro

# Create your views here.

# Rutas
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/Registros/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of Registros'
        },
        {
            'Endpoint': '/Registro/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single Registros object'
        },
        {
            'Endpoint': '/Registros/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new Registros with data sent in post request'
        },
        {
            'Endpoint': '/Registro/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing Registros with data sent in post request'
        },
        {
            'Endpoint': '/Registro/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting Registros'
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getRegistros(request):
    if request.method == 'GET':
        return getRegistrosList(request)
    elif request.method == 'POST':
        return createRegistro(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getRegistro(request, pk):
    if request.method == 'GET':
        return getRegistroDetails(request, pk)
    elif request.method == 'PUT':
        return updateRegistro(request, pk)
    elif request.method == 'DELETE':
        return deleteRegistro(request, pk)