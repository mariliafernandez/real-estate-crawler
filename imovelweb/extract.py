from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import sys
sys.path.append("../")

from src import scrapper

PAGES=10

url = "https://www.imovelweb.com.br/apartamentos-aluguel-sao-paulo-sp-pagina-{}.html"
records = []

for page in range(1, PAGES):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    url_format = url.format(page)
    print(url_format)
    driver.get(url_format)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    cards = soup.find_all('div', class_='sc-i1odl-1 clDfxH')

    for card in cards:
        card_url = scrapper.get_element_attr(card.find('a'), 'href')
        print(card_url)

        price = scrapper.get_element_text(card.find(attrs={'data-qa':'POSTING_CARD_PRICE'}))
        condo = scrapper.get_element_text(card.find(attrs={'data-qa':'expensas'}))
        address = scrapper.get_element_text(card.find(class_='sc-ge2uzh-0 eXwAuU'))
        location = scrapper.get_element_text(card.find(attrs={'data-qa':'POSTING_CARD_LOCATION'}))
        features = scrapper.get_element_text(card.find(attrs={'data-qa':'POSTING_CARD_FEATURES'}))
        title = scrapper.get_element_text(card.find(class_="sc-i1odl-11 kvKUxE"))
        description = scrapper.get_element_text(card.find(attrs={'data-qa':'POSTING_CARD_DESCRIPTION'}))

        images = scrapper.get_elements_attr(card.find(attrs={'data-qa':'POSTING_CARD_GALLERY'}).find_all('img', {"src": True}), 'src')

        records.append({
            "price":price,
            "condo":condo,
            "address":address,
            "location":location,
            "features":features,
            "location":location,
            "title":title,
            "description":description,
            "url":card_url,
            "images":images,
        })

    driver.close()
with open('extracted.json', 'w') as f:
    json.dump(records, f, indent=4)