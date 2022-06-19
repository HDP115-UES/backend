from rest_framework import status
from rest_framework.response import Response
from project_apps.municipio.models import Municipios
from project_apps.municipio.serializers import MunicipioSerializer

# Query o Consulta, retorna una lista completa de objetos 
def getMunicipiosList(request):
    municipio = Municipios.objects.all()
    m_serializer = MunicipioSerializer(municipio, many=True)
    return Response(m_serializer.data, status = status.HTTP_200_OK)

# Create o Crear, crea un nuevo objeto con los datos enviados en el request y lo retorna
def createMunicipio(request):
    m_serializer = MunicipioSerializer(data = request.data)
    if m_serializer.is_valid():
        m_serializer.save()
        return Response(m_serializer.data, status = status.HTTP_201_CREATED)
    return Response(m_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Query o Consulta, retorna un solo objeto especificado por el id
def getMunicipioDetails(request, pk=None):
    municipio = Municipios.objects.filter(id_municipios = pk).first()
    m_serializer = MunicipioSerializer(municipio, many=False)
    return Response(m_serializer.data, status = status.HTTP_200_OK)

# Update o Actualizar, actualiza los datos de un objeto con los datos recibidos en el request y lo retorna
def updateMunicipio(request, pk=None):
    municipio = Municipios.objects.filter(id_municipios = pk).first()
    m_serializer = MunicipioSerializer(municipio, data = request.data)
    if m_serializer.is_valid():
        m_serializer.save()
        return Response(m_serializer.data, status = status.HTTP_200_OK)
    return Response(m_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Delete o Eliminar, elimina un objeto especificado segun su id y retorna un mensaje
def deleteMunicipio(request, pk=None):
    municipio = Municipios.objects.filter(id_municipios = pk).first()
    municipio.delete()
    return Response({'message': 'Eliminado'}, status = status.HTTP_200_OK)