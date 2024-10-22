import function.zara_functions as zara_functions
import function.functions_file as functions_file
from utils.config import ZARA_DATA_FIELDS
from models.product import Product


def get_links(url):
    soup = functions_file.get_soup(url)

    product_blocks = functions_file.get_product_blocks(soup, ZARA_DATA_FIELDS)

    links = []

    for block in product_blocks:
        
        link = zara_functions.get_product_link(block)

        if not link:
            continue

        links.append(link)

    return links

def get_product(link):
    soup_item = functions_file.get_soup(link)

    produtc_name = zara_functions.get_product_name(soup_item, ZARA_DATA_FIELDS)
    product_description = zara_functions.get_product_description(soup_item, ZARA_DATA_FIELDS)
    product_colors_list = zara_functions.get_product_colors(soup_item, ZARA_DATA_FIELDS)
    product_size = zara_functions.get_product_size(soup_item, ZARA_DATA_FIELDS)
    product_price, product_price_old = zara_functions.get_product_price(soup_item, ZARA_DATA_FIELDS)
    product_image_url = zara_functions.get_product_image_url(soup_item, ZARA_DATA_FIELDS)

    produto = Product(
    name=produtc_name,
    description=product_description,
    price=product_price,
    price_old=product_price_old,
    colors=product_colors_list,
    image_url=product_image_url,
    link=link,
    store="ZARA"
    )
    return produto