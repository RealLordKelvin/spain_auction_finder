from django.db import models

# Create your models here.

class auctioninfo(models.Model):
    
    # An MPAN is commonly separated into two sections: the core and the top line data. 
    # The core is the final 13 digits and is the unique identifier.
    identificador = models.CharField(max_length=20)
    tipo_subasta = models.CharField(max_length=20)
    fecha_inicio = models.CharField(max_length=10) # to be handled
    fecha_conclusion = models.CharField(max_length=10)
    tasacion = models.CharField(max_length = 200, null=True, blank = True)
    puja_minima = models.CharField(max_length = 50,null=True, blank = True)
    importe_deposito = models.CharField(max_length = 50,null=True, blank = True)
    cantidad_reclamada = models.CharField(max_length = 50, null=True, blank = True)
    localidad = models.CharField(max_length = 50,null=True, blank = True)
    descripcion = models.CharField(max_length = 300, null=True, blank = True)
   

    '''If user request that there should not be repeated database entries add folowing line below'''
    #unique_together = ["identificador"]
