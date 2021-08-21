from . import handler_scraping
import typing
# Baleares should be a dynamic variable

def scraper(communidad):

    comunidad_content_data_link = handler_scraping.getInformationPageLinkForGivenComunidad(communidad)

    if comunidad_content_data_link == None:
        return None
    result_search_for_comunidad_links = handler_scraping.getSpecificAuctionsLinksForGivenComunidad(comunidad_content_data_link)
    if result_search_for_comunidad_links == None:
        return None
    informationForGivenAuction = handler_scraping.getInformationForGivenAuction(result_search_for_comunidad_links)
    
    print(informationForGivenAuction)
    return informationForGivenAuction


