import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

user = os.getenv('SNOWFLAKE_USER')
password = os.getenv('SNOWFLAKE_PASSWORD')
account = os.getenv('SNOWFLAKE_ACCOUNT')
warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')
database = os.getenv('SNOWFLAKE_DATABASE')
schema = os.getenv('SNOWFLAKE_SCHEMA')

ENGINE = create_engine(
    'snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}'.format(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema
    )
)

ZARA_URLS = ["https://www.zara.com/br/pt/man-special-prices-l806.html?v1=2312656", "https://www.zara.com/br/pt/woman-special-prices-l1314.html?v1=2132535"]

SEPHORA_URL = 'https://www.sephora.com.br/busca/?q=ofertas&pageType=hotsite'

HERING_FEMININO_URL = {
    'Tops': ['https://www.hering.com.br/saldos/feminino/blusas-e-regatas', 'https://www.hering.com.br/saldos/feminino/camisa', 'https://www.hering.com.br/saldos/feminino/jaquetas-e-casacos'],
    'Bottoms': ['https://www.hering.com.br/saldos/feminino/calca', 'https://www.hering.com.br/saldos/feminino/shorts-e-bermudas'],
    'Underwear': ['https://www.hering.com.br/intimates/saldos/pijama-feminino', 'https://www.hering.com.br/intimates/saldos/underwear-feminino'],
    'Dresses': ['https://www.hering.com.br/saldos/feminino/vestido']
}

ZARA_DATA_FIELDS = {
    'product_block': 'product-grid-product _product product-grid-product--ZOOM1-columns product-grid-product',
    'name': 'product-detail-info__header-name',
    'description': 'expandable-text__inner-content',
    'price': 'money-amount__main',
    'colors': 'product-detail-color-selector__colors',
    'colors_name': 'screen-reader-text',
    'image_url': 'product-detail-image-slider__image',
    'link': 'product-detail-info__header-name',
    'created_at': 'product-detail-info__header-name',
    'size': 'product-size-info__main-label',
    'image_url_list': 'media-image__image media__wrapper--media'
}

CATEGORIES_SEPHORA = {
    "makeup": 'Maquiagem',
    "hair": 'Cabelos',
    "perfumery": 'Perfumes',
    "skincare": 'Skincare'
}

ELEMENTS_SEPHORA = {
    'accept_cookies': '//*[@id="onetrust-accept-btn-handler"]',
    'input_search': 'input.impulse-input.impulse-filter-search-input',
    'card_element': 'h3.impulse-card-title',
    'product_element': 'div.impulse-card.impulse-product-card.product.grid',
    'show_more_itens': 'button.impulse-button.submit',
    'brand_element': '//*[@id="product-content"]/div[1]/div/h2/a',
    'product_name': '//*[@id="product-content"]/div[1]/div/div[3]/div/h1',
    'price_standard': 'span.price-standard',
    'price_sales': 'span.price-sales',
    'description': 'div.product-description__text',
    'category': '//*[@id="main"]/div[2]/div/div[2]/a',
    'img': '//*[@id="pdpMain"]/div[1]/div[1]/div[2]/div[2]/div[1]/a/img'
}