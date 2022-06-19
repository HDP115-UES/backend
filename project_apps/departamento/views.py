from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from project_apps.departamento.utils import getDepartamentoDetails, getDepartamentosList, deleteDepartamento, updateDepartamento, createDepartamento

# Create your views here.

# Rutas
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/Departamentos/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of Departamento'
        },
        {
            'Endpoint': '/Departamento/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single Departamento object'
        },
        {
            'Endpoint': '/Departamentos/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new Departamento with data sent in post request'
        },
        {
            'Endpoint': '/Departamento/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing Departamento with data sent in post request'
        },
        {
            'Endpoint': '/Departamento/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting Departamento'
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getDepartamentos(request):
    if request.method == 'GET':
        return getDepartamentosList(request)
    elif request.method == 'POST':
        return createDepartamento(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getDepartamento(request, pk):
    if request.method == 'GET':
        return getDepartamentoDetails(request, pk)
    elif request.method == 'PUT':
        return updateDepartamento(request, pk)
    elif request.method == 'DELETE':
        return deleteDepartamento(request, pk)
        