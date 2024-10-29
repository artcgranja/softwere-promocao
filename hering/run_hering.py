from sqlalchemy.exc import IntegrityError
from driver.selenium_functions import iniciar_selenium
from hering.functions import get_products, get_links
from utils.config import HERING_FEMININO_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def run_hering(session):
    driver = iniciar_selenium()
    products = []

    for category, urls in HERING_FEMININO_URL.items():
        for url in urls:
            driver.get(url)
            try:
                links = get_links(driver)
            except:
                continue
            for link in links:
                produto = get_products(driver, link, category)
                if produto:
                    products.append(produto)
                else:
                    continue
    return products