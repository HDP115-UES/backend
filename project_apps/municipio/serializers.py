from rest_framework.serializers import ModelSerializer
from project_apps.municipio.models import Municipios

# Serializador que combierte los modelos Django a modelos .jason
class MunicipioSerializer(ModelSerializer):
    class Meta:
        model = Municipios
        fields = '__all__'
 