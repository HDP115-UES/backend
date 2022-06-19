from django.db import models

from project_apps.reporte.models import Reportes
from project_apps.usuario.models import Usuarios
# CLase Registros

class Registros(models.Model):
    id_registros = models.AutoField(primary_key= True)
    usuario = models.ForeignKey(Usuarios, on_delete= models.CASCADE, blank=True, null=True)
    reportes = models.ForeignKey(Reportes, on_delete= models.CASCADE, blank=True, null=True)

     # Clase meta para generalizar las tablas
    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        ordering = ['id_registros']

    # Retorna el nombre en forma de cadena
    def __str__(self):
        return self.id_registros
