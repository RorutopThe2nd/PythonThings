from peewee import *
from datetime import datetime

db = SqliteDatabase("products_prices_log.db")


class ProductPriceLog(Model):
    product_name = CharField()
    price = IntegerField()
    log_stamp = DateTimeField(default=datetime.now)

    class Meta:
        database = db


def initialize_db():
    db.connect()
    db.create_tables([ProductPriceLog])


def set_price_history(product_name: str, price: int):
    ProductPriceLog.create(product_name=product_name, price=price)


def get_last_price(product_name: str):
    last_entry = (
        ProductPriceLog.select()
        .where(ProductPriceLog.product_name == product_name)
        .order_by(ProductPriceLog.log_stamp.desc())
        .first()
    )
    return last_entry.price if last_entry else None
