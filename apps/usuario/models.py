from django.db import models

# Create your models here.

class Cliente(models.Model):
    NAT='Natural'
    JUR='Jurídica'
    TIPO_CLIENTE = [
        (NAT,'Natural'),
        (JUR,'Jurídica')
    ]
    nombre=models.CharField(max_length=50, null=True, blank=True)

    apellido= models.CharField(max_length=50, null=True, blank=True)
    cc= models.CharField(max_length=12, null=False,blank=False)
    n_cel= models.CharField(max_length=10, null=False,blank=False)
    tipo=models.CharField(
        max_length=10,
        choices=TIPO_CLIENTE,
        default=NAT
    )

    def __str__(self):
        return '{} {}'.format(self.apellido,self.nombre)


    class Meta:
        verbose_name_plural = "Clientes"
        ordering = ['-id']
