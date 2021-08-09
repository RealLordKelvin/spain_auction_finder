from django.core.management.base import BaseCommand, CommandError
from getauctions.management.scraping.main_scraper import scraper
from typing import Dict, List

from getauctions.models import auctioninfo

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('communidad', type=str, help = 'type in the name of the communidad for which zou want to get the auctions here')
    
    def handle(self, *args, **options):

        help = 'handling to insert the data from the BOE website into the database'

        auctions = scraper(options['communidad'])

        for auction in auctions:
            identificador = auction.get('Identificador')
            comunidad = auction.get('Comunidad')
            tipo_subasta = auction.get('Tipo de subasta')
            fecha_inicio = auction.get('Fecha de inicio').split(' ')[0]
            fecha_conclusion = auction.get('Fecha de conclusión').split(' ')[0]
            tasacion = auction.get('Tasación')
            puja_minima = auction.get('Puja mínima')
            importe_deposito = auction.get('Importe del depósito')
            cantidad_reclamada = auction.get('Cantidad reclamada')
            codigo_postal = auction.get('Localidad').split(' ')[0]
            ciudad = auction.get('Localidad').split(' ')[1]
            Descripcion = auction.get('Descripción')

            totable = auctioninfo(identificador = identificador,
                comunidad = comunidad,
                tipo_subasta = tipo_subasta,
                fecha_inicio = fecha_inicio,
                fecha_conclusion = fecha_conclusion,
                tasacion = tasacion,
                puja_minima = puja_minima,
                importe_deposito = importe_deposito,
                cantidad_reclamada = cantidad_reclamada,
                codigo_postal = codigo_postal,
                ciudad = ciudad,
                descripcion = Descripcion)
            totable.save()
                
            try:
                totable.save()
                # if adding to the database was successful then give feedback
                self.stdout.write(self.style.SUCCESS('Added Auction'))
            except:
                raise CommandError('Auction database dump failed')
            

