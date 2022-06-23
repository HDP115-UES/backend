from rest_framework.serializers import ModelSerializer
from project_apps.usuario.models import Usuarios

# Serializador que combierte los modelos Django a modelos .jason
class UsuariosSerializer(ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

    # Para presentar los datos 
    def to_representation(self, instance):
        return {
            'id_usuarios': instance.id_usuarios,
            'nombre': instance.nombre,
            'apellido': instance.apellido,
            'direccion': instance.direccion,
            'correo': instance.correo,
            'contraseña': instance.contraseña,
            'departamento': instance.departamento.nombre,
            'rol': instance.rol.nombre,
        }