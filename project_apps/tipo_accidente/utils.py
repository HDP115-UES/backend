from rest_framework import status
from rest_framework.response import Response
from project_apps.tipo_accidente.models import TipoAccidente
from project_apps.tipo_accidente.serializers import TipoAccidenteSerializer

# Query o Consulta, retorna una lista completa de objetos 
def getTipoAccidentesList(request):
    tipoAccidentes = TipoAccidente.objects.all()
    tP_serializer = TipoAccidenteSerializer(tipoAccidentes, many=True)
    return Response(tP_serializer.data, status = status.HTTP_200_OK)

# Create o Crear, crea un nuevo objeto con los datos enviados en el request y lo retorna
def createTipoAccidente(request):
    tP_serializer = TipoAccidenteSerializer(data = request.data)
    if tP_serializer.is_valid():
        tP_serializer.save()
        return Response(tP_serializer.data, status = status.HTTP_201_CREATED)
    return Response(tP_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Query o Consulta, retorna un solo objeto especificado por el id
def getTipoAccidentesDetails(request, pk=None):
    tipoAccidentes = TipoAccidente.objects.filter(id_tipo_accidente = pk).first()
    tP_serializer = TipoAccidenteSerializer(tipoAccidentes, many=False)
    return Response(tP_serializer.data, status = status.HTTP_200_OK)

# Update o Actualizar, actualiza los datos de un objeto con los datos recibidos en el request y lo retorna
def updateTipoAccidente(request, pk=None):
    tipoAccidentes = TipoAccidente.objects.filter(id_tipo_accidente = pk).first()
    tP_serializer = TipoAccidenteSerializer(tipoAccidentes, data = request.data)
    if tP_serializer.is_valid():
        tP_serializer.save()
        return Response(tP_serializer.data, status = status.HTTP_200_OK)
    return Response(tP_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Delete o Eliminar, elimina un objeto especificado segun su id y retorna un mensaje
def deleteTipoAccidente(request, pk=None):
    tipoAccidentes = TipoAccidente.objects.filter(id_tipo_accidente = pk).first()
    tipoAccidentes.delete()
    return Response({'message': 'Eliminado'}, status = status.HTTP_200_OK)