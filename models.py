from sqlalchemy import Integer, String, Column, DateTime, Numeric, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(5000), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)

class SalesOrder(Base):
    __tablename__ = 'sales_orders'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    date = Column(DateTime(), nullable=False)

class SalesOrderLine(Base):
    __tablename__ = 'sales_order_lines'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    price = Column(Numeric(10, 2), nullable=False)
    quantity = Column(SmallInteger(), nullable=False)
    product_id = Column(Integer(), ForeignKey('products.id'))
    sales_order_id = Column(Integer(), ForeignKey('sales_orders.id'))
    product = relationship('Product')
    sales_order = relationship('SalesOrder')

def ensure_created(engine):
    Base.metadata.create_all(engine)