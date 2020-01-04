from django.urls import path, include
from . import views as viewsu

app_name= "usuario"
urlpatterns = [

    path('lista', viewsu.ListaUsuarios.as_view() , name='lista'),
    path('nuevo', viewsu.CrearUsuario.as_view() , name='nuevo'),



]
