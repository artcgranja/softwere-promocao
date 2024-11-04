from models.product import Product

class Shoes(Product):
    def __init__(self, name, description, price, price_old, image_url, link, created_at):
        super().__init__(name, description, price, price_old, image_url, link, created_at)
        self.type = 'shoes'

    def __repr__(self):
        return f"<Shoes(name='{self.name}', price={self.price})>"
    
class Tops(Product):
    def __init__(self, name, description, price, price_old, image_url, link, created_at):
        super().__init__(name, description, price, price_old, image_url, link, created_at)
        self.type = 'tops'

    def __repr__(self):
        return f"<Tops(name='{self.name}', price={self.price})>"
    
class Bottoms(Product):
    def __init__(self, name, description, price, price_old, image_url, link, created_at):
        super().__init__(name, description, price, price_old, image_url, link, created_at)
        self.type = 'bottoms'

    def __repr__(self):
        return f"<Bottoms(name='{self.name}', price={self.price})>"
    
class Underwear(Product):
    def __init__(self, name, description, price, price_old, image_url, link, created_at):
        super().__init__(name, description, price, price_old, image_url, link, created_at)
        self.type = 'underwear'

    def __repr__(self):
        return f"<Underwear(name='{self.name}', price={self.price})>"
    
class Dresses(Product):
    def __init__(self, name, description, price, price_old, image_url, link, created_at):
        super().__init__(name, description, price, price_old, image_url, link, created_at)
        self.type = 'dresses'

    def __repr__(self):
        return f"<Dresses(name='{self.name}', price={self.price})>"
    

class Accessories(Product):
    def __init__(self, name, description, price, price_old, image_url, link, created_at):
        super().__init__(name, description, price, price_old, image_url, link, created_at)
        self.type = 'accessories'

    def __repr__(self):
        return f"<Accessories(name='{self.name}', price={self.price})>"