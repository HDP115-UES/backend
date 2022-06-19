from django.urls import path
from project_apps.usuario.views import getUsuario, getUsuarios, getRoutes

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('Usuarios/', getUsuarios, name= 'Usuarios'),
    path('Usuario/<int:pk>/', getUsuario, name="Usuario")
]