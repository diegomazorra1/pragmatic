from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm

class CrearUsuario(CreateView):
    model = Cliente
    template_name = "crear_usuario.html"
    form_class = ClienteForm
    success_url= reverse_lazy('inicio')

class ListaUsuarios(ListView):
    model = Cliente
    template_name="lista_usuarios.html"
