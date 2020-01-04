from django.urls import path, include
from . import views as viewsc

app_name= "cotizacion"
urlpatterns = [

    path('crear/<int:pk>', viewsc.CrearCotizacion.as_view(), name="crear"  ),
    path('lista/cotizaciones', viewsc.ListaCotizacion.as_view(), name="lista_cotizaciones"  ),
    path('editar/<int:pk>', viewsc.UpdateCotizacion.as_view(), name="editar"  ),


]
