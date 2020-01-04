from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Impresora, Papel
from .forms import ImpresoraForm, PapelForm

# Create your views here.
class CrearImpresora(CreateView):
	model= Impresora
	template_name="crear_impresora.html"
	context_object_name = 'obj'
	form_class= ImpresoraForm
	success_url= reverse_lazy("inicio")
	#success_message=" Registrado"

class ListaImpresoras(ListView):
    model = Impresora
    template_name="lista_impresora.html"


class CrearPapel(CreateView):
	model= Impresora
	template_name="crear_papel.html"
	context_object_name = 'obj'
	form_class= PapelForm
	success_url= reverse_lazy("inventario:lista_papeles")
	#success_message=" Registrado"

class ListaPapeles(ListView):
    model = Papel
    template_name="lista_papel.html"


class UpdateImpresora(UpdateView):
	model= Impresora
	template_name="editar_papel.html"
	context_object_name = 'obj'
	form_class= ImpresoraForm
	success_url= reverse_lazy("inventario:lista_impresoras")

class UpdatePapel(UpdateView):
	model= Papel
	template_name="editar_papel.html"
	context_object_name = 'obj'
	form_class= PapelForm
	success_url= reverse_lazy("inventario:lista_papeles")
