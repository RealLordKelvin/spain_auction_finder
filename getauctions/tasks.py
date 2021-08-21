from __future__ import absolute_import, unicode_literals

from django.core.management.base import BaseCommand, CommandError
from getauctions.management.scraping.main_scraper import scraper
from getauctions.models import AuctionInfo
from celery import shared_task

def load_auction_data_to_database(auctions):
    for auction in auctions:
        identificador = auction.get('Identificador')
        direccion = auction.get('Dirección')
        provincia = auction.get('Provincia')    
        tipo_subasta = auction.get('Tipo de subasta')
        fecha_inicio = auction.get('Fecha de inicio').split(' ')[0]
        fecha_conclusion = auction.get('Fecha de conclusión').split(' ')[0]
        tasacion = auction.get('Tasación')
        puja_minima = auction.get('Puja mínima')
        importe_deposito = auction.get('Importe del depósito')
        cantidad_reclamada = auction.get('Cantidad reclamada')
        codigo_postal = auction.get('Código Postal')
        ciudad = auction.get('Localidad')
        correo_electronico = auction.get('Correo electrónico')
        descripcion = auction.get('Descripción')

        totable = AuctionInfo(identificador = identificador,
            direccion = direccion,
            provincia = provincia,
            tipo_subasta = tipo_subasta,
            fecha_inicio = fecha_inicio,
            fecha_conclusion = fecha_conclusion,
            tasacion = tasacion,
            puja_minima = puja_minima,
            importe_deposito = importe_deposito,
            cantidad_reclamada = cantidad_reclamada,
            codigo_postal = codigo_postal,
            ciudad = ciudad,
            correo_electronico = correo_electronico,
            descripcion = descripcion,
            )
                
        try:
            totable.save()
            BaseCommand.stdout.write(BaseCommand.style.SUCCESS('Added Auction'))
                # if adding to the database was successful then give feedbac
        except:
            BaseCommand.stdout.write(BaseCommand.style.WARNING('Auction Adding Failed'))
            pass

@shared_task
def calling_scraper():
    provincias = ['Albacete', 'Avila', 'Alicante', 'Almeria', 'Baleares', 'Badajoz', 
                    'Barcelona', 'Burgos','Caceres', 'Cadiz', 'Castellon', 'Ciudad Real',
                    'Cordoba', 'A Coruña', 'Cuenca', 'Gerona', 'Granada', 'Guadalajara',
                     'Guipúzcoa', 'Huelva', 'Huesca', 'Jaén', 'Leon', 'Lérida', 'La Rioja',
                     'Lugo', 'Madrid', 'Malaga', 'Murcia', 'Navarra', 'Orense', 'Asturias',
                     'Palencia', 'Las Palmas', 'Ponteverda', 'Salamanca', 'Santa Cruz de Tenerifa',
                     'Cantabria', 'Segovia', 'Sevilla', 'Soria', 'Tarragona', 'Teruel', 'Toledo',
                     'Valencia', 'Valladolid', 'Vizcaya', 'Zamora', 'Zaragoza', 'Ceuta', 'Melilla']
    results = []
    
    for provincia in provincias:
        scrapingAuctionInfos = scraper(provincia)
        try:
            load_auction_data_to_database(scrapingAuctionInfos)
        except:
            print('WARNING')

    return


