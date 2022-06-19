from rest_framework import status
from rest_framework.response import Response
from project_apps.departamento.models import Departamentos
from project_apps.departamento.serializers import DepartamentoSerializers

# Query o Consulta, retorna una lista completa de objetos 
def getDepartamentosList(request):
    departamento = Departamentos.objects.all()
    d_serializer = DepartamentoSerializers(departamento, many=True)
    return Response(d_serializer.data, status = status.HTTP_200_OK)

# Create o Crear, crea un nuevo objeto con los datos enviados en el request y lo retorna
def createDepartamento(request):
    d_serializer = DepartamentoSerializers(data = request.data)
    if d_serializer.is_valid():
        d_serializer.save()
        return Response(d_serializer.data, status = status.HTTP_201_CREATED)
    return Response(d_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Query o Consulta, retorna un solo objeto especificado por el id
def getDepartamentoDetails(request, pk=None):
    departamento = Departamentos.objects.filter(id_departamentos = pk).first()
    d_serializer = DepartamentoSerializers(departamento, many=False)
    return Response(d_serializer.data, status = status.HTTP_200_OK)

# Update o Actualizar, actualiza los datos de un objeto con los datos recibidos en el request y lo retorna
def updateDepartamento(request, pk=None):
    departamento = Departamentos.objects.filter(id_departamentos = pk).first()
    d_serializer = DepartamentoSerializers(departamento, data = request.data)
    if d_serializer.is_valid():
        d_serializer.save()
        return Response(d_serializer.data, status = status.HTTP_200_OK)
    return Response(d_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Delete o Eliminar, elimina un objeto especificado segun su id y retorna un mensaje
def deleteDepartamento(request, pk=None):
    departamento = Departamentos.objects.filter(id_departamentos = pk).first()
    departamento.delete()
    return Response({'message': 'Eliminado'}, status = status.HTTP_200_OK)