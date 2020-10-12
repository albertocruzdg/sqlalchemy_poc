from datetime import datetime
from models import ensure_created, Product, SalesOrder, SalesOrderLine

from dbcontext import DbContext

from query_objects import ProductQueryObject

def add_single(session):
    product = Product(name="Ford Focus Mk III", description="Cool hatchback car")
    session.add(product)
    session.commit()

def add_multiple(session):
    product = Product(name="Ford Ranger", description="Pick-up")

    sales_order = SalesOrder(date=datetime.now())
    sales_order_line = SalesOrderLine(price=20000, quantity=1, product=product,sales_order=sales_order)

    session.add_all([product, sales_order, sales_order_line])
    session.commit()

def cheaper_than(session, price):
    query = ProductQueryObject(session)
    query.cheaper_than(price)
    products = query.run()

    for product in products:
        print(product.id, product.name, product.description, product.price)

def all_products(session):
    products = session.query(Product).all()
    for i in products:
        print(i.id, i.name, i.description)
# add_single(session)
# add_multiple(session)
# all_products(session)


context = DbContext()
session = context.get_session()
cheaper_than(session, 6000)