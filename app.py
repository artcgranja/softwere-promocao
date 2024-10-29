from sqlalchemy.orm import sessionmaker
from models.product import Base
from utils.config import ENGINE
from zara.run_zara import run_zara
from hering.run_hering import run_hering
from sqlalchemy.exc import IntegrityError

Base.metadata.create_all(ENGINE)

Session = sessionmaker(bind=ENGINE)
session = Session()

def main():
    products_zara = run_zara(session)
    products_hering = run_hering(session)

    commit_products(products_zara)
    commit_products(products_hering)

def commit_products(products):
    session.add_all(products)
    try:
        session.commit()
        return print(f"Produtos adicionados com sucesso: {len(products)}")
    except IntegrityError:
        session.rollback()
        print("Erro ao inserir produtos. Algum produto pode já existir no banco de dados.")

if __name__ == "__main__":
    main()