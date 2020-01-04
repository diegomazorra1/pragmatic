from django import forms
from .models import Cotizacion


class CotizacionForm(forms.ModelForm):

    class Meta:
        model = Cotizacion

        fields = [
        'cliente',
        'notintas',
        'ancho',
        'largo',
        'tipo_impresion' ,
        'maquina_impresion' ,
        'modo_impresion',
        'tipo_papel' ,
        'noetiquetas',
        'costo_operador',
        'porc_utilidad',
        'porc_desperdicio',
        'costo',


        ]
        labels = {

                'cliente': 'Cliente',
                'notintas': ' Numero  de tintas',
                'ancho':  'Ancho',
                'largo':   'Largo',
                'tipo_impresion': 'Tipo de impresión',
                'maquina_impresion': 'Tipo de Maquina de impresión',
                'modo_impresion': 'Modo de impresion',
                'tipo_papel': 'Tipo de Papel',
                'noetiquetas': 'Numero de etiquetas',
                'costo_operador': 'Costo del operador ',
                'porc_utilidad': 'Porcentaje de utilidad',
                'porc_desperdicio': 'Desperdicio',
                'costo': 'Costo',


        }
        widgets= {


                'cliente': forms.Select(attrs= {'class': 'form-control'}  )  ,
                'notintas': forms.TextInput(attrs= {'class': 'form-control'}  )  ,
                'ancho': forms.TextInput(attrs= {'class': 'form-control', 'placeholder':'in' }  )  ,
                'largo': forms.TextInput(attrs= {'class': 'form-control', 'placeholder':'in'}  )  ,
                'maquina_impresion': forms.Select(attrs= {'class': 'form-control'}  )  ,
                'modo_impresion': forms.Select(attrs= {'class': 'form-control'}  )  ,
                'tipo_impresion': forms.Select(attrs= {'class': 'form-control'}  )  ,
                'tipo_papel': forms.Select(attrs= {'class': 'form-control'}  )  ,
                'noetiquetas': forms.TextInput(attrs= {'class': 'form-control'}  )  ,
                'costo_operador': forms.TextInput(attrs= {'class': 'form-control', 'placeholder':'Pesos/Hora' }  )  ,
                'porc_utilidad': forms.TextInput(attrs= {'class': 'form-control','placeholder':'%'}  )  ,
                'porc_desperdicio': forms.TextInput(attrs= {'class': 'form-control','placeholder':'Pulgadas','readonly': True}  )  ,
                'costo': forms.TextInput(attrs= {'class': 'form-control', 'readonly': True}  )  ,

        }
