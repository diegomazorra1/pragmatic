from django.urls import path, include
from . import views as viewsi

app_name= "inventario"
urlpatterns = [

    path('crear/impresora', viewsi.CrearImpresora.as_view(), name="crear_impresora"  ),
    path('lista/impresoras', viewsi.ListaImpresoras.as_view(), name="lista_impresoras"  ),
    path('editar/impresora/<int:pk>', viewsi.UpdateImpresora.as_view(), name="editar_impresora"  ),
    path('crear/papel', viewsi.CrearPapel.as_view(), name="crear_papel"  ),
    path('lista/papel', viewsi.ListaPapeles.as_view(), name="lista_papeles"  ),
    path('editar/papel/<int:pk>', viewsi.UpdatePapel.as_view(), name="editar_papel"  ),




]
