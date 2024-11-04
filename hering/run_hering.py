from hering.functions import get_products, get_links
from utils.config import HERING_URLS
from utils.util_functions import remover_duplicados_por_link

def run_hering(driver):
    products = []

    for category, urls in HERING_URLS.items():
        for gender, urls in urls.items():
            for url in urls:
                driver.get(url)
                try:
                    links = get_links(driver)
                except:
                    continue
                for link in links:
                    produto = get_products(driver, link, category, gender)
                    if produto:
                        products.append(produto)
                    else:
                        continue
    return remover_duplicados_por_link(products)