from rest_framework import status
from rest_framework.response import Response
from project_apps.usuario.models import Usuarios
from project_apps.usuario.serializers import UsuariosSerializer

# Query o Consulta, retorna una lista completa de objetos 
def getUsuariosList(request):
    usuario = Usuarios.objects.all()
    u_serializer = UsuariosSerializer(usuario, many=True)
    return Response(u_serializer.data, status = status.HTTP_200_OK)

# Create o Crear, crea un nuevo objeto con los datos enviados en el request y lo retorna
def createUsuario(request):
    u_serializer = UsuariosSerializer(data = request.data)
    if u_serializer.is_valid():
        u_serializer.save()
        return Response(u_serializer.data, status = status.HTTP_201_CREATED)
    return Response(u_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Query o Consulta, retorna un solo objeto especificado por el id
def getUsuariosDetails(request, pk=None):
    usuario = Usuarios.objects.filter(id_usuarios = pk).first()
    u_serializer = UsuariosSerializer(usuario, many=False)
    return Response(u_serializer.data, status = status.HTTP_200_OK)

# Update o Actualizar, actualiza los datos de un objeto con los datos recibidos en el request y lo retorna
def updateUsuario(request, pk=None):
    usuario = Usuarios.objects.filter(id_usuarios = pk).first()
    u_serializer = UsuariosSerializer(usuario, data = request.data)
    if u_serializer.is_valid():
        u_serializer.save()
        return Response(u_serializer.data, status = status.HTTP_200_OK)
    return Response(u_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Delete o Eliminar, elimina un objeto especificado segun su id y retorna un mensaje
def deleteUsuario(request, pk=None):
    usuario = Usuarios.objects.filter(id_usuarios = pk).first()
    usuario.delete()
    return Response({'message': 'Eliminado'}, status = status.HTTP_200_OK)