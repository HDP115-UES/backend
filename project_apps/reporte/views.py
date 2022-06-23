from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from project_apps.reporte.utils import getReporteDetails, getReportesList, updateReporte, deleteReporte, createReporte
# Create your views here.

# Rutas
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/Reportes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of Reporte'
        },
        {
            'Endpoint': '/Reporte/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single Reporte object'
        },
        {
            'Endpoint': '/Reportes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new Reporte with data sent in post request'
        },
        {
            'Endpoint': '/Reporte/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing Reporte with data sent in post request'
        },
        {
            'Endpoint': '/Reporte/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting Reporte'
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def getReportes(request):
    if request.method == 'GET':
        
        return getReportesList(request)
    elif request.method == 'POST':
        return createReporte(request)

@api_view(['GET', 'PUT', 'DELETE'])
def getReporte(request, pk):
    if request.method == 'GET':
        return getReporteDetails(request, pk)
    elif request.method == 'PUT':
        return updateReporte(request, pk)
    elif request.method == 'DELETE':
        return deleteReporte(request, pk)
