from rest_framework.serializers import ModelSerializer
from project_apps.registro.models import Reportes

# Serializador que combierte los modelos Django a modelos .jason
class ReporteSerializer(ModelSerializer):
    class Meta:
        model = Reportes
        fields = '__all__'