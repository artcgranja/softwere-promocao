import zara.zara_functions as zara_functions
import zara.functions_file as functions_file
from models.product import Product


def get_links(url, store):
    soup = functions_file.get_soup(url)

    product_blocks = functions_file.get_product_blocks(soup, store)

    links = []

    for block in product_blocks:
        
        link = zara_functions.get_product_link(block)

        if not link:
            continue

        links.append(link)

    return links

def get_product(link, elements, gender=None):
    soup_item = functions_file.get_soup(link)

    produtc_name = zara_functions.get_product_name(soup_item, elements)
    product_description = zara_functions.get_product_description(soup_item, elements)
    product_price, product_price_old = zara_functions.get_product_price(soup_item, elements)
    product_image_url = zara_functions.get_product_image_url(soup_item, elements)

    produto = Product(
    name=produtc_name,
    description=product_description,
    price=product_price,
    price_old=product_price_old,
    image_url=product_image_url,
    link=link,
    category='Nan',
    store="ZARA",
    gender=gender
    )
    return produto