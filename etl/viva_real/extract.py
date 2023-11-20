import requests
from bs4 import BeautifulSoup
import json

import sys

sys.path.append("../")

from src import scrapper

PAGES = 10

url_base = "https://www.vivareal.com.br/aluguel/sp/sao-paulo/?pagina={}#onde=,S%C3%A3o%20Paulo,S%C3%A3o%20Paulo,,,,,city,BR%3ESao%20Paulo%3ENULL%3ESao%20Paulo,,,"
base_href_viva = "https://www.vivareal.com.br"

records = []

for page in range(1, PAGES):
    url = url_base.format(page)

    print(url)
    
    r = requests.get(
        url.format(page),
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
        },
    )

    soup = BeautifulSoup(r.text, "html.parser")
    content_list = soup.find_all("article", class_="property-card__container")

    for card in content_list:

        card_url = scrapper.get_element_attr(card.find("a", class_="property-card__content-link"), 'href')
        print(card_url)

        title = scrapper.get_element_text(card.find("span", class_="property-card__title"))
        address = scrapper.get_element_text(card.find("span", class_="property-card__address-container"))
        area = scrapper.get_element_text(card.find("li", class_="property-card__detail-area"))
        room = scrapper.get_element_text(card.find("li", class_="property-card__detail-room"))
        bathroom = scrapper.get_element_text(card.find("li", class_="property-card__detail-bathroom"))
        garage = scrapper.get_element_text(card.find("li", class_="property-card__detail-garage"))
        amenities = [scrapper.get_element_text(el) for el in card.find_all("li", class_="amenities__item")]
        
        images = scrapper.get_elements_attr(card.find_all('img', {'src':True}), 'src')
        price = scrapper.get_element_text(card.find("div", class_="property-card__price"))

        condo = scrapper.get_element_text(card.find(class_="property-card__price-details--condo"))

        obj = {
            "url": card_url,
            "title": title,
            "address": address,
            "area": area,
            "room": room,
            "bathroom": bathroom,
            "garage": garage,
            "amenities": amenities,
            "price": price,
            "condo": condo
        }

        records.append(obj)


with open('extracted.json', 'w') as f:
    json.dump({"records":records}, f, indent=4)