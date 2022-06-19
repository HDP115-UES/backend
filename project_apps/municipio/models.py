from django.db import models

# Clase Municipios

class Municipios(models.Model):
    id_municipios = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 100, unique=True, blank=True, null=True)

    # Clase meta para generalizar las tablas
    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        ordering = ['id_municipios']

    # Retorna el nombre en forma de cadena
    def __str__(self):
        return self.nombre