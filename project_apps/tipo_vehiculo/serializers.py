from rest_framework.serializers import ModelSerializer
from project_apps.tipo_vehiculo.models import TipoVehiculo

# Serializador que combierte los modelos Django a modelos .jason
class TipoVehiculoSerializer(ModelSerializer):
    class Meta:
        model = TipoVehiculo
        fields = '__all__'