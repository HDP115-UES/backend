from distutils.command.upload import upload
from django.db import models

from project_apps.departamento.models import Departamentos
from project_apps.accidente.models import Accidentes
# Clase Reportes

class Reportes(models.Model):
    id_reporte = models.AutoField(primary_key= True)
    fecha_accidente = models.DateField(auto_now_add= True)
    hora_accidente =models.TimeField(auto_now_add= True)
    numero_involucrados = models.IntegerField(blank=True, null=True)
    imagen = models.ImageField(upload_to='posts%Y/%m/%d', null= True, blank=True, verbose_name='Imagen del accidente')
    accidente = models.ForeignKey(Accidentes, on_delete= models.CASCADE, null= False, blank= False)
    departamento = models.ForeignKey(Departamentos, on_delete= models.CASCADE, null= False, blank= False)
    
    # Clase meta para generalizar las tablas
    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'
        ordering = ['id_reporte']

    # Retorna el -- en forma de cadena
    def __str__(self):
        return self.id_reporte