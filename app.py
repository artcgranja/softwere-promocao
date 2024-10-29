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
    products_zara = run_zara(driver)
    products_hering = run_hering(driver)
    products_sephora = run_sephora(driver)

    commit_products(products_zara)
    commit_products(products_hering)
    commit_products(products_sephora)

def commit_products(products):
    session.add_all(products)
    try:
        session.commit()
        return print(f"Produtos adicionados com sucesso: {len(products)}")
    except IntegrityError:
        session.rollback()
        print("Erro ao inserir produtos. Algum produto pode já existir no banco de dados.")

if __name__ == "__main__":
    main(driver)