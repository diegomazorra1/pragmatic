from django.db import models
from apps.usuario.models import Cliente
from apps.inventario.models import Impresora, Papel
# Create your models here.


class Cotizacion(models.Model):
    cliente= models.ForeignKey(Cliente,on_delete=models.CASCADE)
    notintas=models.IntegerField()
    ancho=models.FloatField(default=0)
    largo=models.FloatField(default=0)
    modos_impresion=(('a lo largo','a lo largo'),('a lo ancho','a lo ancho'))
    area= models.FloatField(null=True,blank=True)
    modo_impresion= models.CharField(choices=modos_impresion,default="a lo largo",max_length=12,blank=False,null=False)
    tiempo_impresion= models.DecimalField(default=0,max_digits=9, decimal_places=3)
    tipos_impresion=(('Digital','Digital'),('Flexografica','Flexografica'))
    tipo_impresion=models.CharField(choices=tipos_impresion,default="Digital",max_length=12,blank=False,null=False)
    maquina_impresion= models.ForeignKey(Impresora,on_delete=models.CASCADE, blank=False)
    tipo_papel= models.ForeignKey(Papel,on_delete=models.CASCADE, blank= False )

    noetiquetas= models.IntegerField( blank=False)
    costo_operador= models.IntegerField(null=True)

    porc_utilidad= models.IntegerField( blank=False)
    porc_desperdicio= models.DecimalField(default=0,max_digits=9, decimal_places=3)
    costo= models.DecimalField(default=0,max_digits=9, decimal_places=3)
    class Meta:
        verbose_name_plural = "Clientes"
        ordering = ['-id']

    def save(self,*args, **kwargs):
        papel= Papel.objects.get(id=self.tipo_papel_id)
        impresora= Impresora.objects.get(id=self.maquina_impresion_id)
        self.area= self.ancho*self.largo
        print(self.tiempo_impresion)
        if self.modo_impresion=="a lo largo":
            arriba_etiqueta=self.largo
            arriba_etiqueta_inicial=self.largo
            abajo_etiqueta=self.ancho
            abajo_etiqueta_inicial=self.ancho
            print("LARGO")

        else:
            arriba_etiqueta=self.ancho
            arriba_etiqueta_inicial=self.ancho
            abajo_etiqueta=self.largo
            abajo_etiqueta_inicial=self.largo
            print("ANCHO")

        n=0
        p=0

        while impresora.largo_rodillo > arriba_etiqueta:
            n+=1
            arriba_etiqueta=arriba_etiqueta_inicial*n
            
            if impresora.largo_rodillo<= arriba_etiqueta:

                break
            else:
                continue


        ancho_etiquetas=arriba_etiqueta_inicial*n

        print("ancho_etiquetas",ancho_etiquetas)

        desperdicio_ancho=  impresora.largo_rodillo- ancho_etiquetas

        print("numero de etiqueta",n)
        print("desperdicio ancho",desperdicio_ancho)
        for i in range(0,self.noetiquetas,n):
            p+=1
            print(p)

        print("abajo_etiqueta_inicial",abajo_etiqueta_inicial)

        largo_papel=abajo_etiqueta_inicial*p
        etiquetas_barrido=p*n
        print("largo_papel",largo_papel)
        print("n",n)
        desperdicio_etiquetas=(etiquetas_barrido-self.noetiquetas)*self.area
        desperdicio_area= desperdicio_ancho*largo_papel
        desperdicio_total= desperdicio_etiquetas+desperdicio_area
        print("noetiquetas",self.noetiquetas)



        print("desperdicio_etiquetas",desperdicio_etiquetas)


        self.porc_desperdicio=desperdicio_total

        self.tiempo_impresion=((largo_papel*(1/39.37))/impresora.velocidad_imp)


        if self.tipo_impresion=="Digital":
            self.costo= ((self.largo*self.ancho*(1/1550.0031))*self.noetiquetas*papel.costo) + (self.tiempo_impresion*self.costo_operador)
            self.costo = (self.costo*(self.porc_utilidad/100)+self.costo)
        else:
            area=(self.largo*self.ancho*(1/1550.0031))
            self.costo= ((area + desperdicio_area )*self.noetiquetas*papel.costo) + (impresora.tiempo_pre*self.costo_operador*self.notintas) +(self.tiempo_impresion*self.costo_operador)

        return super(Cotizacion, self).save( *args, **kwargs)
