from rest_framework.serializers import ModelSerializer
from project_apps.departamento.models import Departamentos

# Serializador que combierte los modelos Django a modelos .jason
class DepartamentoSerializers(ModelSerializer):
    class Meta:
        model = Departamentos	
        fields = '__all__'
        