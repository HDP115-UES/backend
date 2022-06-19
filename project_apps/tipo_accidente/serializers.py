from rest_framework.serializers import ModelSerializer
from project_apps.tipo_accidente.models import TipoAccidente

# Serializador que combierte los modelos Django a modelos .jason
class TipoAccidenteSerializer(ModelSerializer):
    class Meta:
        model = TipoAccidente
        fields = '__all__'
