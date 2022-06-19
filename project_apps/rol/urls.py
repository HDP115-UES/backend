from django.urls import path
from project_apps.rol.views import getRoles, getRol, getRoutes

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('Roles/', getRoles, name= 'Roles'),
    path('Rol/<int:pk>/', getRol, name="Rol")
]