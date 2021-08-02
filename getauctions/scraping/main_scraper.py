import handler_scraping
# Baleares should be a dynamic variable

if __name__ == "__main__":
    comunidad_content_data_link = handler_scraping.getInformationPageLinkForGivenComunidad('Baleares')

    result_search_for_comunidad_links = handler_scraping.getSpecificAuctionsLinksForGivenComunidad(comunidad_content_data_link)

    informationForGivenAuction = handler_scraping.getInformationForGivenAuction(result_search_for_comunidad_links)

    print(informationForGivenAuction)
