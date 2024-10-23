from sqlalchemy.orm import sessionmaker
from models.product import Base
from utils.config import ENGINE

Base.metadata.create_all(ENGINE)

Session = sessionmaker(bind=ENGINE)
session = Session()