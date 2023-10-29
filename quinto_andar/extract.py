from bs4 import BeautifulSoup
import json
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

sys.path.append("../")

from src import scrapper

LOAD_MORE = 20

url = "https://www.quintoandar.com.br/alugar/imovel/sao-paulo-sp-brasil"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(url)

# Load more data by clicking on button
btn = driver.find_element(By.XPATH, '//button[@aria-label="Ver mais"]')
i = 0
while btn and i < LOAD_MORE:
    try:
        btn.click()
    except:
        break

    html = driver.page_source
    btn = driver.find_element(By.XPATH, '//button[@aria-label="Ver mais"]')
    i += 1

# Save html page w/ all content 
with open('page_source.html', 'w') as f:
    f.write(html)


# Read html page, scrap data and stores it in json file 
soup = BeautifulSoup(html, "html.parser")
cards = soup.find_all(class_="MuiCard-root")

records = []
for card in cards:
    card_url = scrapper.get_element_attr(card.find("a"), "href")

    images = scrapper.get_elements_attr(card.find_all("img", {"src": True}), "src")

    address = scrapper.get_element_text(
        card.find(attrs={"data-testid": "house-card-address"})
    )

    region = scrapper.get_element_text(
        card.find(attrs={"data-testid": "house-card-region"})
    )

    area = scrapper.get_element_text(
        card.find(attrs={"data-testid": "house-card-area"})
    )

    bedroom = scrapper.get_element_text(
        card.find(attrs={"data-testid": "house-card-bedrooms"})
    )

    price = scrapper.get_element_text(
        card.find(attrs={"data-testid": "house-card-rent"})
    )

    records.append(
        {
            "url": card_url,
            "images": images,
            "address": address,
            "region": region,
            "area": area,
            "bedroom": bedroom,
            "price": price,
        }
    )

with open("extracted.json", "w") as f:
    json.dump(records, f, indent=4)
