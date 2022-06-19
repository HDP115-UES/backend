from rest_framework import status
from rest_framework.response import Response
from project_apps.reporte.models import Reportes
from project_apps.reporte.serializers import ReporteSerializer

# Query o Consulta, retorna una lista completa de objetos 
def getReportesList(request):
    reporte = Reportes.objects.all()
    r_serializer = ReporteSerializer(reporte, many=True)
    return Response(r_serializer.data, status = status.HTTP_200_OK)

# Create o Crear, crea un nuevo objeto con los datos enviados en el request y lo retorna
def createReporte(request):
    r_serializer = ReporteSerializer(data = request.data)
    if r_serializer.is_valid():
        r_serializer.save()
        return Response(r_serializer.data, status = status.HTTP_201_CREATED)
    return Response(r_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Query o Consulta, retorna un solo objeto especificado por el id
def getReporteDetails(request, pk=None):
    reporte = Reportes.objects.filter(id_reporte = pk).first()
    r_serializer = ReporteSerializer(reporte, many=False)
    return Response(r_serializer.data, status = status.HTTP_200_OK)

# Update o Actualizar, actualiza los datos de un objeto con los datos recibidos en el request y lo retorna
def updateReporte(request, pk=None):
    reporte = Reportes.objects.filter(id_reporte = pk).first()
    r_serializer = ReporteSerializer(reporte, data = request.data)
    if r_serializer.is_valid():
        r_serializer.save()
        return Response(r_serializer.data, status = status.HTTP_200_OK)
    return Response(r_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Delete o Eliminar, elimina un objeto especificado segun su id y retorna un mensaje
def deleteReporte(request, pk=None):
    reporte = Reportes.objects.filter(id_reporte = pk).first()
    reporte.delete()
    return Response({'message': 'Eliminado'}, status = status.HTTP_200_OK)