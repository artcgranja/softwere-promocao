from utils.config import ZARA_URLS, ZARA_DATA_FIELDS
from zara.data_functions import get_product, get_links
from utils.util_functions import remover_duplicados_por_link

def run_zara(driver):
    urls = ZARA_URLS
    products = []
    for gender, url in urls.items():
        links = get_links(url, ZARA_DATA_FIELDS)
        for link in links:
            product = get_product(link, ZARA_DATA_FIELDS, gender)
            if product.link not in [p.link for p in products]:
                products.append(product)
    return remover_duplicados_por_link(products)