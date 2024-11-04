from sqlalchemy.orm import sessionmaker
from models.product import Base
from utils.config import ENGINE
from zara.run_zara import run_zara
from hering.run_hering import run_hering
from sephora.run_sephora import run_sephora
from driver.selenium_functions import iniciar_selenium
from sqlalchemy.exc import IntegrityError

Base.metadata.create_all(ENGINE)

Session = sessionmaker(bind=ENGINE)
session = Session()

driver = iniciar_selenium()

def main(driver):
    products_sephora = run_sephora(driver)
    products_zara = run_zara(driver)
    products_hering = run_hering(driver)
    products_all = products_sephora + products_zara + products_hering

    commit_products(products_all)

def commit_products(products):
    try:
        for product in products:
            session.add(product)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
                print("Erro ao inserir produtos. Algum produto pode já existir no banco de dados.")
                continue
    except Exception as e:
        print(f"Erro ao adicionar produtos: {e}")
    finally:
        print(f"Produtos adicionados com sucesso: {len(products)}")

if __name__ == "__main__":
    main(driver)