from django.db import models

# Clase Rol

class Rol(models.Model):
    id_rol = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 100, unique=True, blank=True, null=True)

    # Clase meta para generalizar las tablas
    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        ordering = ['id_rol']

    # Retorna el nombre en forma de cadena
    def __str__(self):
        return self.nombre