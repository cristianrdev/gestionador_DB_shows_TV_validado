from django.urls import path     
from . import views
urlpatterns = [
    path('', views.redireccionar),
    path('shows', views.listar_shows),
    path('shows/new', views.nuevo_show),	
    path('shows/<id>', views.detalle_show),
    path('shows/<id>/edit', views.editar_show),
    path('delete/<id>', views.borrar_show),

]