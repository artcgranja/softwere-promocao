from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from models.product import Base, Product
from utils.config import ZARA_URLS, ENGINE
from function.data_functions import get_product, get_links
from datetime import datetime, timezone

Base.metadata.create_all(ENGINE)

Session = sessionmaker(bind=ENGINE)
session = Session()

if __name__ == "__main__":
    urls = ZARA_URLS
    products = []
    today = datetime.now(timezone.utc).date()
    for url in urls:
        links = get_links(url)
        for link in links:
            product = get_product(link)
            if product.link not in [p.link for p in products]:
                products.append(product)

    session.add_all(products)

    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        print("Erro ao inserir produtos. Algum produto pode já existir no banco de dados.")
    finally:
        session.close()