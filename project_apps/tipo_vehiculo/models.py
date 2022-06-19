from django.db import models

# Clase TipoVehiculos

class TipoVehiculo(models.Model):
    id_tipo_vehiculo = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 100, unique=True, blank=True, null=True)

    # Clase meta para generalizar las tablas
    class Meta:
        verbose_name = 'TipoVehiculo'
        verbose_name_plural = 'TipoVehiculos'
        ordering = ['id_tipo_vehiculo']
    
    # Retorna el nombre en forma de cadena
    def __str__(self):
        return self.nombre
