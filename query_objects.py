from models import Product

class ProductQueryObject:
    def __init__(self, session):
        self.query = session.query(Product)

    def cheaper_than(self, price):
        self.query = self.query.filter(Product.price <= price)

    def run(self):
        return self.query.all()