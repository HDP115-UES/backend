from rest_framework import status
from rest_framework.response import Response
from project_apps.tipo_vehiculo.models import TipoVehiculo
from project_apps.tipo_vehiculo.serializers import TipoVehiculoSerializer

# Query o Consulta, retorna una lista completa de objetos 
def getTipoVehiculosList(request):
    tipoVehiculo = TipoVehiculo.objects.all()
    tV_serializer = TipoVehiculoSerializer(tipoVehiculo, many=True)
    return Response(tV_serializer.data, status = status.HTTP_200_OK)

# Create o Crear, crea un nuevo objeto con los datos enviados en el request y lo retorna
def createTipoVehiculo(request):
    tV_serializer = TipoVehiculoSerializer(data = request.data)
    if tV_serializer.is_valid():
        tV_serializer.save()
        return Response(tV_serializer.data, status = status.HTTP_201_CREATED)
    return Response(tV_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Query o Consulta, retorna un solo objeto especificado por el id
def getTipoVehiculosDetails(request, pk=None):
    tipoVehiculo = TipoVehiculo.objects.filter(id_tipo_vehiculo = pk).first()
    tP_serializer = TipoVehiculoSerializer(tipoVehiculo, many=False)
    return Response(tP_serializer.data, status = status.HTTP_200_OK)

# Update o Actualizar, actualiza los datos de un objeto con los datos recibidos en el request y lo retorna
def updateTipoVehiculo(request, pk=None):
    tipoVehiculo = TipoVehiculo.objects.filter(id_tipo_vehiculo = pk).first()
    tV_serializer = TipoVehiculoSerializer(tipoVehiculo, data = request.data)
    if tV_serializer.is_valid():
        tV_serializer.save()
        return Response(tV_serializer.data, status = status.HTTP_200_OK)
    return Response(tV_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Delete o Eliminar, elimina un objeto especificado segun su id y retorna un mensaje
def deleteTipoVehiculos(request, pk=None):
    tipoVehiculo = TipoVehiculo.objects.filter(id_tipo_vehiculo = pk).first()
    tipoVehiculo.delete()
    return Response({'message': 'Eliminado'}, status = status.HTTP_200_OK)