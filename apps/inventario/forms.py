from django import forms
from .models import Impresora, Papel


class ImpresoraForm(forms.ModelForm):

    class Meta:
        model = Impresora

        fields = [
        'nombre',
        'tiempo_pre',
        'largo_rodillo',
        'velocidad_imp',



        ]
        labels = {

                'nombre': ' Referencia de impresora',
                'tiempo_pre': 'Tiempo de preparacion ',
                'largo_rodillo': 'Largo del rodillo ' ,
                'velocidad_imp':  'Velocidad de impresion ' ,


        }
        widgets= {

                'nombre': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Referencia' }  )  ,
                'tiempo_pre': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Horas' }  )  ,
                'largo_rodillo':   forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Pulgadas'}  ) ,
                'velocidad_imp':  forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Pulgadas/Minuto'}  ),

        }

class PapelForm(forms.ModelForm):

    class Meta:
        model = Papel

        fields   = [
        'nombre',
        'costo',




        ]
        labels = {

                'nombre': ' Referencia ',
                'costo': 'Costo ',



        }
        widgets= {

                'nombre': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Referencia' }  )  ,
                'costo': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Pesos/m2' }  )  ,


        }
