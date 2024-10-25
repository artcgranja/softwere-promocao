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

SEPHORA_URL = {
    'maquiagem': 'https://www.sephora.com.br/busca/?q=ofertas&pageType=hotsite&filter=discrete%3A1%3A105&page=1',
    'perfumes': 'https://www.sephora.com.br/busca/?q=ofertas&pageType=hotsite&filter=discrete%3A1%3A82&page=1',
    'cabelos': 'https://www.sephora.com.br/busca/?q=ofertas&pageType=hotsite&filter=discrete%3A1%3A58&page=1',
    'skincare': 'https://www.sephora.com.br/busca/?q=ofertas&pageType=hotsite&filter=discrete%3A1%3A4&page=1',
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

HERING_FEMININO_URL = {
    'Tops': ['https://www.hering.com.br/saldos/feminino/blusas-e-regatas', 'https://www.hering.com.br/saldos/feminino/camisa', 'https://www.hering.com.br/saldos/feminino/jaquetas-e-casacos'],
    'Bottoms': ['https://www.hering.com.br/saldos/feminino/calca', 'https://www.hering.com.br/saldos/feminino/shorts-e-bermudas'],
    'Underwear': ['https://www.hering.com.br/intimates/saldos/pijama-feminino', 'https://www.hering.com.br/intimates/saldos/underwear-feminino'],
    'Dresses': ['https://www.hering.com.br/saldos/feminino/vestido']
}