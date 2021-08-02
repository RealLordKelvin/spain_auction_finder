from django.core.management.base import BaseCommand, CommandError
from getauctions.management.scraping.main_scraper import scraping
from typing import Dict, List

from getauctions.models import auctioninfo

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('communidad', type=str, help = 'type in the name of the communidad for which zou want to get the auctions here')
    
    def handle(self, *args, **options):

        help = 'handling to insert the data from the BOE website into the database'

        auctions:Dict = scraping(options['communidad'])
        '''
        identificador = models.CharField(max_length=20)
        tipo_subasta = models.CharField(max_length=20)
        fecha_inicio = models.CharField(max_length=10) # to be handled
        fecha_conclusion = models.CharField(max_length=10)
        tasacion = models.CharField(max_length = 200)
        puja_minima = models.CharField(max_length = 50)
        importe_deposito = models.CharField(max_length = 50)
        cantidad_reclamada = models.CharField(max_length = 50)
        localidad = models.CharField(max_length = 50)
        Descripcion = models.CharField(max_length = 300)
   
        '''
        for auction in auctions:
            identificador = auction.get('Identificador')
            tipo_subasta = auction.get('Tipo de subasta')
            fecha_inicio = auction.get('Fecha de inicio').split(' ')[0]
            fecha_conclusion = auction.get('Fecha de conclusión').split(' ')[0]
            tasacion = auction.get('Tasación')
            puja_minima = auction.get('Puja mínima')
            importe_deposito = auction.get('Importe del depósito')
            cantidad_reclamada = auction.get('Cantidad reclamada')
            localidad = auction.get('Localidad')
            Descripcion = auction.get('Descripción')

            auction = auctioninfo(identificador = identificador,
                tipo_subasta = tipo_subasta,
                fecha_inicio = fecha_inicio,
                fecha_conclusion = fecha_conclusion,
                tasacion = tasacion,
                puja_minima = puja_minima,
                importe_deposito = importe_deposito,
                cantidad_reclamada = cantidad_reclamada,
                localidad = localidad,
                descripcion = Descripcion)
            auction.save()
            
            try:
                auction.save()
                # if adding to the database was successful then give feedback
                self.stdout.write(self.style.SUCCESS('Added Meter'))
            except:
                raise CommandError('Flow File database dump failed')
            

