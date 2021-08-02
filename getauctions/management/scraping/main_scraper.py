import handler_scraping
import typing
# Baleares should be a dynamic variable

if __name__ == "__main__":

    def scraping(communidad:str = 'Baleares'):

        comunidad_content_data_link = handler_scraping.getInformationPageLinkForGivenComunidad(communidad)

        result_search_for_comunidad_links = handler_scraping.getSpecificAuctionsLinksForGivenComunidad(comunidad_content_data_link)

        informationForGivenAuction = handler_scraping.getInformationForGivenAuction(result_search_for_comunidad_links)

        return informationForGivenAuction
