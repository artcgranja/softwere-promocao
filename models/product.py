from sqlalchemy import Column, Integer, String, Float, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone
import uuid

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(String(36), primary_key=True)
    name = Column(String(16777216), nullable=False)
    description = Column(String(16777216))
    price = Column(Float, nullable=False)
    price_old = Column(Float)
    image_url = Column(String(16777216))
    link = Column(String(16777216), nullable=False)
    gender = Column(String(16777216))
    category = Column(String(16777216), nullable=False)
    store = Column(String(16777216), nullable=False)
    datetime = Column(TIMESTAMP)

    def __init__(self, name, description, price, price_old, image_url, link, category, store, gender):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.price = price
        self.price_old = price_old
        self.image_url = image_url
        self.store = store
        self.link = link
        self.gender = gender
        self.category = category
        self.datetime = datetime.now(timezone.utc).strftime('%Y-%m-%d')