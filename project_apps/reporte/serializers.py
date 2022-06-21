from rest_framework.serializers import ModelSerializer
from project_apps.registro.models import Reportes

# Serializador que combierte los modelos Django a modelos .jason
class ReporteSerializer(ModelSerializer):

    class Meta:
        model = Reportes
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id_reporte': instance.id_reporte,
            'fecha_accidente': instance.fecha_accidente,
            'hora_accidente': instance.hora_accidente,
            'numero_involucrados': instance.numero_involucrados,
            'imagen': instance.imagen if instance.imagen != '' else '',
            'accidente': instance.accidente.descripción,
            'departamento': instance.departamento.nombre,
        }