from sqlalchemy import Column, Integer, String, Float, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone
import uuid

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(16777216), nullable=False)
    description = Column(String(16777216))
    price = Column(Float, nullable=False)
    price_old = Column(Float)
    colors = Column(String(16777216))
    image_url = Column(String(16777216))
    store = Column(String(16777216), nullable=False)
    link = Column(String(16777216), nullable=False)
    datetime = Column(TIMESTAMP, default=lambda: datetime.now(timezone.utc))

    def __init__(self, name, description, price, price_old, colors, image_url, store, link):
        self.name = name
        self.description = description
        self.price = price
        self.price_old = price_old
        self.colors = colors
        self.image_url = image_url
        self.store = store
        self.link = link
        self.datetime = datetime.now(timezone.utc)

    def __repr__(self):
        return f"<Product(name='{self.name}', price='{self.price}', store='{self.store}')>"
