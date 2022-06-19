from django.db import models

# Clase tipo Accidente

class TipoAccidente(models.Model):
    id_tipo_accidente = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 200, unique=True, blank=True, null=True)

    # Clase meta para generalizar las tablas
    class Meta:
        verbose_name = 'TipoAccidente'
        verbose_name_plural = 'TipoAccidentes'
        ordering = ['id_tipo_accidente']

    # Retorna el nombre en forma de cadena
    def __str__(self):
        return self.nombre