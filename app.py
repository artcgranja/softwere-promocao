from sqlalchemy.orm import sessionmaker
from models.product import Base
from utils.config import ENGINE
from zara.run_zara import run_zara
from hering.run_hering import run_hering

Base.metadata.create_all(ENGINE)

Session = sessionmaker(bind=ENGINE)
session = Session()

#zara = run_zara(session)
hering = run_hering(session)