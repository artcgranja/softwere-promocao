from sqlalchemy.exc import IntegrityError
from utils.config import ZARA_URLS, ZARA_DATA_FIELDS
from zara.data_functions import get_product, get_links

def run_zara(session):
    urls = ZARA_URLS
    products = []
    for url in urls:
        links = get_links(url, ZARA_DATA_FIELDS)
        for link in links:
            product = get_product(link, ZARA_DATA_FIELDS)
            if product.link not in [p.link for p in products]:
                products.append(product)

    session.add_all(products)

    try:
        session.commit()
        return print(f"Produtos adicionados com sucesso: {len(products)}")
    except IntegrityError:
        session.rollback()
        print("Erro ao inserir produtos. Algum produto pode já existir no banco de dados.")