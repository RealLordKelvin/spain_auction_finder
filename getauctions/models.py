from django.db import models

# Create your models here.

class AuctionInfo(models.Model):
    
    identificador = models.CharField(max_length=50)
    direccion = models.CharField(max_length = 100,null=True, blank = True)
    provincia = models.CharField(max_length = 25,null=True, blank = True)
    tipo_subasta = models.CharField(max_length=50)
    fecha_inicio = models.CharField(max_length=10) # to be handled
    fecha_conclusion = models.CharField(max_length=10)
    tasacion = models.CharField(max_length = 200, null=True, blank = True)
    puja_minima = models.CharField(max_length = 50,null=True, blank = True)
    importe_deposito = models.CharField(max_length = 50,null=True, blank = True)
    cantidad_reclamada = models.CharField(max_length = 50, null=True, blank = True)
    codigo_postal = models.CharField(max_length = 5, null=True, blank = True)
    ciudad = models.CharField(max_length = 50,null=True, blank = True)
    correo_electronico = models.CharField(max_length = 300,null=True, blank = True)
    descripcion = models.CharField(max_length = 1000, null=True, blank = True)

    class Meta:
      verbose_name_plural = "Auctions"
      unique_together = ["identificador"]

    def __str__(self):
        return self.identificador
   

    '''If user request that there should not be repeated database entries add folowing line below'''
  
