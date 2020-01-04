from django.db import models

# Create your models here.


class Impresora(models.Model):
    nombre = models.CharField(max_length=20, null=True, blank=True )
    tiempo_pre= models.IntegerField()
    largo_rodillo= models.IntegerField()
    velocidad_imp= models.IntegerField()
    def __str__(self):
        return '{} '.format(self.nombre)
    class Meta:

        ordering = ['-id']

class Papel(models.Model):
    nombre=models.CharField(max_length=50)
    costo= models.IntegerField()
    def __str__(self):
        return '{}'.format(self.nombre)
    class Meta:

        ordering = ['-id']
