from rest_framework.serializers import ModelSerializer
from project_apps.registro.models import Reportes

# Serializador que combierte los modelos Django a modelos .jason
class ReporteSerializer(ModelSerializer):

    class Meta:
        model = Reportes
        fields = '__all__'

    # Para presentar los datos 
    def to_representation(self, instance):
        return {
            'id_reporte': instance.id_reporte,
            'fecha_accidente': instance.fecha_accidente,
            'hora_accidente': instance.hora_accidente,
            'numero_involucrados': instance.numero_involucrados,
            'imagen': instance.imagen if instance.imagen != '' else '',
            'tipo_vehiculo': instance.tipo_vehiculo.nombre,
            'tipo_accidente': instance.tipo_accidente.nombre,
            'departamento': instance.departamento.nombre,
            'descripción': instance.descripción,
        }