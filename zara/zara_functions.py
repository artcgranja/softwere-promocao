from babel.numbers import parse_decimal

def get_product_link(product_block):
    try:
        product_link = product_block.find('a')['href']
    except:
        product_link = None
    return product_link

def get_product_name(product_block, fields):
    product_name = product_block.find(class_=fields['name']).next_element.strip()
    return product_name

def get_product_price(product_block, fields):
    try:
        product_price = product_block.find_all(class_=fields['price'])
        price = product_price[1].text.strip()
        price_old = product_price[0].text.strip()
        price = float(parse_decimal(price.replace("R$", "").strip(), locale='pt_BR'))
        price_old = float(parse_decimal(price_old.replace("R$", "").strip(), locale='pt_BR'))
    except:
        price = float(0)
        price_old = float(0)
    return price, price_old

def get_product_image_url(product_block, fields):
    """ainda pensando como pegar a imagem"""
    product_image_url = product_block.find_all(class_=fields['image_url_list'])
    return None

def get_product_description(product_block, fields):
    product_description = product_block.find(class_=fields['description']).text.strip()
    return product_description