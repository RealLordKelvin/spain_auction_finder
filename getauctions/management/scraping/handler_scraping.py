from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np
import requests
from requests import get
import re
from typing import List

def _getWebsiteConnection(page_url: str):

    try:
        conn = requests.get(page_url)
    except:
        raise ValueError('connection to website was not possible, check the url of the website')
    soup = BeautifulSoup(conn.text, 'html.parser')

    return soup

def getInformationPageLinkForGivenComunidad(comunidad:str, LINK_BOE_URL = 'https://subastas.boe.es')->str:
    
    conn_boe = _getWebsiteConnection(LINK_BOE_URL)
    comunidadValue = _comunidad_value_finder(comunidad)
    comunidad_content_name = conn_boe.find('option', attrs={'value': comunidadValue})
    comunidad_content = conn_boe.find('area', attrs={'title': comunidad_content_name.text})
    comunidad_content_data_link = LINK_BOE_URL + comunidad_content.attrs['href']
    comunidad_content_data_link = comunidad_content_data_link.strip()
    
    return comunidad_content_data_link


def _comunidad_value_finder(comunidad:str)->str:
    
    comunidad = comunidad.lower()
    
    if comunidad == 'Alava'.lower() or comunidad == 'Ávala'.lower():
        value = '01'
    elif comunidad == 'Albacete'.lower():
        value = '02'
    elif comunidad == 'Alicante'.lower():
        value = '03'
    elif comunidad == 'Almeria'.lower() or comunidad == 'Almería'.lower():
        value = '04'
    elif comunidad == 'Avila'.lower() or comunidad == 'Ávila'.lower():
        value = '05'
    elif comunidad == 'Badajoz'.lower():
        value = '06'
    elif comunidad == 'Baleares'.lower():
        value = '07'
    elif comunidad == 'Barcelona'.lower():
        value = '08'
    elif comunidad == 'Burgos'.lower():
        value = '09'
    elif comunidad == 'Caceres'.lower() or comunidad == 'Cáceres'.lower():
        value = '10'
    elif comunidad == 'Cadiz'.lower() or comunidad == 'Cádiz'.lower():
        value = '11'
    elif comunidad == 'Castellon'.lower() or comunidad == 'Castellón'.lower():
        value = '12'
    elif comunidad == 'Ciudad Real'.lower():
        value = '13'
    elif comunidad == 'Cordoba'.lower() or comunidad == 'Córdoba'.lower():
        value = '14'
    elif comunidad == 'A Coruña'.lower() or comunidad == 'La Coruña'.lower():
        value = '15'
    elif comunidad == 'Cuenca'.lower():
        value = '16'
    elif comunidad == 'Gerona'.lower():
        value = '17'
    elif comunidad == 'Granada'.lower():
        value = '18'
    elif comunidad == 'Guadalajara'.lower():
        value = '19'
    elif comunidad == 'Guipúzcoa'.lower() or comunidad == 'Guipuzcoa'.lower():
        value = '20'
    elif comunidad == 'Huelva'.lower():
        value = '21'
    elif comunidad == 'Huesca'.lower():
        value = '22'
    elif comunidad == 'Jaén'.lower() or comunidad == 'Jaen'.lower():
        value = '23'
    elif comunidad == 'Leon'.lower() or comunidad == 'León'.lower():
        value = '24'
    elif comunidad == 'Lérida'.lower() or comunidad == 'Lerida'.lower():
        value = '25'
    elif comunidad == 'La Rioja'.lower():
        value = '26'
    elif comunidad == 'Lugo'.lower():
        value = '27'
    elif comunidad == 'Madrid'.lower():
        value = '28'
    elif comunidad == 'Malaga'.lower() or comunidad == 'Málaga'.lower():
        value = '29'
    elif comunidad == 'Murcia'.lower():
        value = '30'
    elif comunidad == 'Navarra'.lower():
        value = '31'
    elif comunidad == 'Orense'.lower():
        value = '32'
    elif comunidad == 'Asturias'.lower():
        value = '33'
    elif comunidad == 'Palencia'.lower():
        value = '34'
    elif comunidad == 'Las Palmas'.lower():
        value = '35'
    elif comunidad == 'Ponteverda'.lower():
        value = '36'
    elif comunidad == 'Salamanca'.lower():
        value = '37'
    elif comunidad == 'Santa Cruz de Tenerifa'.lower():
        value = '38'
    elif comunidad == 'Cantabria'.lower():
        value = '39'
    elif comunidad == 'Segovia'.lower():
        value = '40'
    elif comunidad == 'Sevilla'.lower():
        value = '41'
    elif comunidad == 'Soria'.lower():
        value = '42'
    elif comunidad == 'Tarragona'.lower():
        value = '43'
    elif comunidad == 'Teruel'.lower():
        value = '44'
    elif comunidad == 'Toledo'.lower():
        value = '45'
    elif comunidad == 'Valencia'.lower():
        value = '46'
    elif comunidad == 'Valladolid'.lower():
        value = '47'
    elif comunidad == 'Vizcaya'.lower():
        value = '48'
    elif comunidad == 'Zamora'.lower():
        value = '49'
    elif comunidad == 'Zaragoza'.lower():
        value = '50'
    elif comunidad == 'Ceuta'.lower():
        value = '51'
    elif comunidad == 'Melilla'.lower():
        value = '52'
    else:
        raise ValueError('Comunidad name not found')
    
    return value


def getSpecificAuctionsLinksForGivenComunidad(comunidad_content_data_link:str, LINK_BOE_URL = 'https://subastas.boe.es')->List[str]:

    conn_comunidad = _getWebsiteConnection(comunidad_content_data_link)
    comunidad_content = conn_comunidad.find_all('a',attrs={'class': 'resultado-busqueda-link-defecto'},href=True)# attrs={'title': comunidad})
    resultado_busqueda_link_collector = []

    for result in range(len(comunidad_content)):
        link = LINK_BOE_URL + str(comunidad_content[result].attrs['href'])[1:]
        link = link.strip()
        resultado_busqueda_link_collector.append(link)

    return resultado_busqueda_link_collector

def getInformationForGivenAuction(resultado_busqueda_link_collector:List[str]):
    
    auctionsInformationList = []
    for auctionLink in resultado_busqueda_link_collector:
        conn_auction = _getWebsiteConnection(auctionLink)
        navList = _getNavListLinks(conn_auction)
        for link in range(len(navList)):
            if link == 0:
                table_info = _getTableInformation(conn_auction)
            else:
                conn_auction = _getWebsiteConnection(navList[link])
                try:
                    t = _getTableInformation(conn_auction)
                    table_info.update(t)
                except:
                    continue
        auctionsInformationList.append(table_info)
    return auctionsInformationList

def _getTableInformation(connection):
    
    table = connection.find('table')
    auctionTable = pd.read_html(str(table))
    auctionTableDictionary = auctionTable[0].to_dict()
    auctionTableDictionary = list(auctionTableDictionary.values())
    
    tableInfo = dict()
    myKeys = list(auctionTableDictionary[0].values())
    myValues = list(auctionTableDictionary[1].values())

    for i in range(len(myKeys)):
        tableInfo[myKeys[i]] = myValues[i]
    return tableInfo
    

def _getNavListLinks(connection, LINK_BOE_URL = 'https://subastas.boe.es')->List[str]:
    
    navListLinks = []
    for ul in connection.find_all('ul', class_='navlist'):
        for li in ul.find_all('li'):
            a = li.find('a')
            navListLinks.append(LINK_BOE_URL + str(a['href'])[1:])
    return navListLinks