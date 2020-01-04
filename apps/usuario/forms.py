from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields = [
        'tipo',
        'nombre',
        'apellido',
        'cc' ,
        'n_cel' ,

        ]
        labels = {
                'tipo': 'Tipo de Cliente',
                'nombre': 'Nombre' ,
                'apellido':  'Apellidos' ,
                'cc': 'Numero de Cedula o Nit' ,

        }

        widgets= {
                'tipo': forms.Select(attrs= {'class': 'form-control'}  )  ,
                'nombre': forms.TextInput(attrs= {'class': 'form-control'}  )  ,
                'apellido':   forms.TextInput(attrs= {'class': 'form-control'}  ) ,
                'cc':  forms.TextInput(attrs= {'class': 'form-control'}  ),
                'n_cel':  forms.TextInput(attrs= {'class': 'form-control'}  ),

        }
