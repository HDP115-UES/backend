from rest_framework.serializers import ModelSerializer
from project_apps.usuario.models import Usuarios

# Serializador que combierte los modelos Django a modelos .jason
class UsuariosSerializer(ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'