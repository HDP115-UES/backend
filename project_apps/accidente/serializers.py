from rest_framework.serializers import ModelSerializer
from project_apps.accidente.models import Accidentes

# Serializador que combierte los modelos Django a modelos .jason
class AccidenteSerializer(ModelSerializer):
    class Meta:
        model = Accidentes
        fields = '__all__'