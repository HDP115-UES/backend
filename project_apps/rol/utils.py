from rest_framework import status
from rest_framework.response import Response
from project_apps.rol.models import Rol
from project_apps.rol.serializers import RolSerializer

# Query o Consulta, retorna una lista completa de objetos 
def getRolesList(request):
    rol = Rol.objects.all()
    r_serializer = RolSerializer(rol, many=True)
    return Response(r_serializer.data, status = status.HTTP_200_OK)

# Create o Crear, crea un nuevo objeto con los datos enviados en el request y lo retorna
def createRol(request):
    r_serializer = RolSerializer(data = request.data)
    if r_serializer.is_valid():
        r_serializer.save()
        return Response(r_serializer.data, status = status.HTTP_201_CREATED)
    return Response(r_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Query o Consulta, retorna un solo objeto especificado por el id
def getRolesDetails(request, pk=None):
    rol = Rol.objects.filter(id_rol = pk).first()
    r_serializer = RolSerializer(rol, many=False)
    return Response(r_serializer.data, status = status.HTTP_200_OK)

# Update o Actualizar, actualiza los datos de un objeto con los datos recibidos en el request y lo retorna
def updateRol(request, pk=None):
    rol = Rol.objects.filter(id_rol = pk).first()
    r_serializer = RolSerializer(rol, data = request.data)
    if r_serializer.is_valid():
        r_serializer.save()
        return Response(r_serializer.data, status = status.HTTP_200_OK)
    return Response(r_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Delete o Eliminar, elimina un objeto especificado segun su id y retorna un mensaje
def deleteRol(request, pk=None):
    rol = Rol.objects.filter(id_rol = pk).first()
    rol.delete()
    return Response({'message': 'Eliminado'}, status = status.HTTP_200_OK)