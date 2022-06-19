from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from project_apps.rol.utils import getRolesList, getRolesDetails, updateRol, deleteRol, createRol

# Create your views here.

# Rutas
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/Roles/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of Roles'
        },
        {
            'Endpoint': '/Rol/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single Roles object'
        },
        {
            'Endpoint': '/Roles/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new Roles with data sent in post request'
        },
        {
            'Endpoint': '/Rol/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing Roles with data sent in post request'
        },
        {
            'Endpoint': '/Rol/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting Roles'
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getRoles(request):
    if request.method == 'GET':
        return getRolesList(request)
    elif request.method == 'POST':
        return createRol(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getRol(request, pk):
    if request.method == 'GET':
        return getRolesDetails(request, pk)
    elif request.method == 'PUT':
        return updateRol(request, pk)
    elif request.method == 'DELETE':
        return deleteRol(request, pk)
        