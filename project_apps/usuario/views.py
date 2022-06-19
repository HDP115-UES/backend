from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from project_apps.usuario.utils import getUsuariosDetails, getUsuariosList, deleteUsuario, updateUsuario, createUsuario

# Create your views here.

# Rutas
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/Usuarios/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of Usuarios'
        },
        {
            'Endpoint': '/Usuario/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single Usuarios object'
        },
        {
            'Endpoint': '/Usuario/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new Usuarios with data sent in post request'
        },
        {
            'Endpoint': '/Usuario/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing Usuarios with data sent in post request'
        },
        {
            'Endpoint': '/Usuario/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting Usuarios'
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getUsuarios(request):
    if request.method == 'GET':
        return getUsuariosList(request)
    elif request.method == 'POST':
        return createUsuario(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getUsuario(request, pk):
    if request.method == 'GET':
        return getUsuariosDetails(request, pk)
    elif request.method == 'PUT':
        return updateUsuario(request, pk)
    elif request.method == 'DELETE':
        return deleteUsuario(request, pk)
