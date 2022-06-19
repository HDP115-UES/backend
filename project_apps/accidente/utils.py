from rest_framework import status
from rest_framework.response import Response
from project_apps.accidente.models import Accidentes
from project_apps.accidente.serializers import AccidenteSerializer

# Query o Consulta, retorna una lista completa de objetos 
def getAccidentesList(request):
    accidente = Accidentes.objects.all()
    a_serializer = AccidenteSerializer(accidente, many=True)
    return Response(a_serializer.data, status = status.HTTP_200_OK)

# Create o Crear, crea un nuevo objeto con los datos enviados en el request y lo retorna
def createAccidente(request):
    a_serializer = AccidenteSerializer(data = request.data)
    if a_serializer.is_valid():
        a_serializer.save()
        return Response(a_serializer.data, status = status.HTTP_201_CREATED)
    return Response(a_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Query o Consulta, retorna un solo objeto especificado por el id
def getAccidenteDetails(request, pk=None):
    accidente = Accidentes.objects.filter(id_accidente = pk).first()
    a_serializer = AccidenteSerializer(accidente, many=False)
    return Response(a_serializer.data, status = status.HTTP_200_OK)

# Update o Actualizar, actualiza los datos de un objeto con los datos recibidos en el request y lo retorna
def updateAccidente(request, pk=None):
    accidente = Accidentes.objects.filter(id_accidente = pk).first()
    a_serializer = AccidenteSerializer(accidente, data = request.data)
    if a_serializer.is_valid():
        a_serializer.save()
        return Response(a_serializer.data, status = status.HTTP_200_OK)
    return Response(a_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Delete o Eliminar, elimina un objeto especificado segun su id y retorna un mensaje
def deleteAccidente(request, pk=None):
    accidente = Accidentes.objects.filter(id_accidente = pk).first()
    accidente.delete()
    return Response({'message': 'Eliminado'}, status = status.HTTP_200_OK)