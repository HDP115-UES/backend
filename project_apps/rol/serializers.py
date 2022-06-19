from rest_framework.serializers import ModelSerializer
from project_apps.rol.models import Rol

# Serializador que combierte los modelos Django a modelos .jason
class RolSerializer(ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'
