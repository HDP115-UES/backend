from django.urls import path
from project_apps.accidente.views import getAccidente, getAccidentes, getRoutes

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('Accidentes/', getAccidentes, name= 'Accidentes'),
    path('Accidente/<int:pk>/', getAccidente, name="Accidente")
]