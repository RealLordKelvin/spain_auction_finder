from django.db import models

# Create your models here.

class AuctionInfo(models.Model):
    
    # An MPAN is commonly separated into two sections: the core and the top line data. 
    # The core is the final 13 digits and is the unique identifier.
    identificador = models.CharField(max_length=20)
    comunidad = models.CharField(max_length = 25)
    tipo_subasta = models.CharField(max_length=20)
    fecha_inicio = models.CharField(max_length=10) # to be handled
    fecha_conclusion = models.CharField(max_length=10)
    tasacion = models.CharField(max_length = 200, null=True, blank = True)
    puja_minima = models.CharField(max_length = 50,null=True, blank = True)
    importe_deposito = models.CharField(max_length = 50,null=True, blank = True)
    cantidad_reclamada = models.CharField(max_length = 50, null=True, blank = True)
    codigo_postal = models.CharField(max_length = 5, default = '')
    ciudad = models.CharField(max_length = 50,null=True, blank = True, default = '')
    descripcion = models.CharField(max_length = 300, null=True, blank = True)

    class Meta:
      verbose_name_plural = "Auctions"

    def __str__(self):
        return self.identificador
   

    '''If user request that there should not be repeated database entries add folowing line below'''
    unique_together = ["identificador"]
