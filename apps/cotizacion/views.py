from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Cotizacion
from .forms import CotizacionForm


# Create your views here.


class PagPrincipal(TemplateView):

	template_name="base.html"

class CrearCotizacion(CreateView):
	model=Cotizacion
	template_name="registro_cotizacion.html"
	context_object_name = 'obj'
	form_class= CotizacionForm
	success_url= reverse_lazy("inicio")
	#success_message=" Registrado"
	def get_initial(self):
		initial = super().get_initial()
		initial['cliente'] = self.kwargs['pk']
		return initial

class ListaCotizacion(ListView):
	model= Cotizacion
	template_name="lista_cotizacion.html"


class UpdateCotizacion(UpdateView):
	model = Cotizacion
	template_name = 'registro_cotizacion.html'
	form_class = CotizacionForm
	success_url = reverse_lazy('cotizacion:lista_cotizaciones')
