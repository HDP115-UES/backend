from rest_framework import status
from rest_framework.response import Response
from project_apps.registro.models import Registros
from project_apps.registro.serializers import RegistrosSerializer

# Query o Consulta, retorna una lista completa de objetos 
def getRegistrosList(request):
    registro = Registros.objects.all()
    rg_serializer = RegistrosSerializer(registro, many=True)
    return Response(rg_serializer.data, status = status.HTTP_200_OK)

# Create o Crear, crea un nuevo objeto con los datos enviados en el request y lo retorna
def createRegistro(request):
    rg_serializer = RegistrosSerializer(data = request.data)
    if rg_serializer.is_valid():
        rg_serializer.save()
        return Response(rg_serializer.data, status = status.HTTP_201_CREATED)
    return Response(rg_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Query o Consulta, retorna un solo objeto especificado por el id
def getRegistroDetails(request, pk=None):
    registro = Registros.objects.filter(id_registros = pk).first()
    rg_serializer = RegistrosSerializer(registro, many=False)
    return Response(rg_serializer.data, status = status.HTTP_200_OK)

# Update o Actualizar, actualiza los datos de un objeto con los datos recibidos en el request y lo retorna
def updateRegistro(request, pk=None):
    registro = Registros.objects.filter(id_registros = pk).first()
    rg_serializer = RegistrosSerializer(registro, data = request.data)
    if rg_serializer.is_valid():
        rg_serializer.save()
        return Response(rg_serializer.data, status = status.HTTP_200_OK)
    return Response(rg_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Delete o Eliminar, elimina un objeto especificado segun su id y retorna un mensaje
def deleteRegistro(request, pk=None):
    registro = Registros.objects.filter(id_registros = pk).first()
    registro.delete()
    return Response({'message': 'Eliminado'}, status = status.HTTP_200_OK)