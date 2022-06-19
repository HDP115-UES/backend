from rest_framework.serializers import ModelSerializer
from project_apps.registro.models import Registros

# Serializador que combierte los modelos Django a modelos .jason
class RegistrosSerializer(ModelSerializer):
    class Meta:
        model = Registros
        fields = '__all__'