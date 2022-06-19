from tabnanny import verbose
from django.db import models

from project_apps.municipio.models import Municipios

#Clase Departamentos

class Departamentos(models.Model):
    id_departamentos = models.AutoField(primary_key= True)
    Municipios = models.ForeignKey(Municipios, on_delete= models.CASCADE, null= False, blank= False)
    nombre = models.CharField(max_length= 100,  unique=True, blank=True, null=True)

    # Clase meta para generalizar las tablas
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['id_departamentos']

    # Retorna el nombre en forma de cadena
    def __str__(self):
        return self.nombre