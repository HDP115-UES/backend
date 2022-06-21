from tabnanny import verbose
from django.db import models

from project_apps.tipo_accidente.models import TipoAccidente
from project_apps.tipo_vehiculo.models import TipoVehiculo

#Clase Accidentes

class Accidentes(models.Model):
    id_accidente = models.AutoField(primary_key= True)
    descripción = models.CharField(max_length= 500,  blank=True, null=True)
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete= models.CASCADE, null= False, blank= False)
    tipo_accidente = models.ForeignKey(TipoAccidente, on_delete= models.CASCADE, null= False, blank= False)

    # Clase meta para generalizar las tablas
    class Meta:
        verbose_name = 'Accidente'
        verbose_name_plural = 'Accidentes'
        ordering = ['id_accidente']

    # Retorna el nombre en forma de cadena
    def __str__(self):
        return self.descripción 