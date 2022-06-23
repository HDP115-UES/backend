from pyexpat import model
from django.db import models

from project_apps.departamento.models import Departamentos
from project_apps.rol.models import Rol

#Clase Usuarios
class Usuarios(models.Model):
    id_usuarios = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length= 100)
    apellido = models.CharField(max_length= 120)
    direccion = models.CharField(max_length= 300, unique=True, blank=True, null=True)
    correo = models.EmailField(max_length= 200, unique=True, blank=True, null=True)
    contraseña = models.CharField(max_length= 100)
    departamento = models.ForeignKey(Departamentos, on_delete= models.CASCADE, null= False, blank= False)
    rol = models.ForeignKey(Rol, on_delete= models.CASCADE, null= False, blank= False)

    # Clase meta para generalizar las tablas
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id_usuarios']

    # Retorna el nombre en forma de cadena
    def __str__(self):
        return self.nombre