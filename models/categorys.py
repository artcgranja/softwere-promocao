from models.product import Product

class Shoes(Product):
    def __init__(self, name, description, price, price_old, colors, image_url, link, created_at, size):
        super().__init__(name, description, price, price_old, colors, image_url, link, created_at)
        self.type = 'shoes'
        self.size = size

    def __repr__(self):
        return f"<Shoes(name='{self.name}', price={self.price})>"
    
class Tops(Product):
    def __init__(self, name, description, price, price_old, colors, image_url, link, created_at, size):
        super().__init__(name, description, price, price_old, colors, image_url, link, created_at)
        self.type = 'tops'
        self.size = size

    def __repr__(self):
        return f"<Tops(name='{self.name}', price={self.price})>"
    
class Bottoms(Product):
    def __init__(self, name, description, price, price_old, colors, image_url, link, created_at, size):
        super().__init__(name, description, price, price_old, colors, image_url, link, created_at)
        self.type = 'bottoms'
        self.size = size

    def __repr__(self):
        return f"<Bottoms(name='{self.name}', price={self.price})>"
    
class Accessories(Product):
    def __init__(self, name, description, price, price_old, colors, image_url, link, created_at):
        super().__init__(name, description, price, price_old, colors, image_url, link, created_at)
        self.type = 'accessories'

    def __repr__(self):
        return f"<Accessories(name='{self.name}', price={self.price})>"