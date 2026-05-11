import csv
from dataclasses import asdict, fields
import re
import time
from typing import List

from pydantic import BaseModel
from bs4 import BeautifulSoup
import undetected as uc
import pandas as pd


class ProductContainer(BaseModel):
    title: str
    price: int
    rating: float
    owner: str | None
    city: str | None


driver = uc.Chrome()

# try:
URL = "https://www.tokopedia.com/find/rtx-4060-laptop?utm_source=google&utm_medium=organic&utm_campaign=find"
driver.get(URL)

time.sleep(1)

soup = BeautifulSoup(driver.page_source, "html.parser")
containers = soup.find_all("div", attrs={"class": "css-15vayma"})
products: List[ProductContainer] = []

for container in containers:
    title_el = container.find("span", attrs={"class": "+tnoqZhn89+NHUA43BpiJg=="})
    price_el = container.find("div", string=re.compile("Rp"))  # type: ignore
    rating_el = container.find("span", attrs={"class": "_2NfJxPu4JC-55aCJ8bEsyw=="})
    creatorContainer_el = container.find(
        "div", attrs={"class": "_1yoE8Ml3qwvn-r+EZ5hlbA=="}
    )

    title = title_el.text if title_el else "Unknown Title"

    raw_price = 0
    if price_el and price_el.text:
        raw_price = int(str(price_el.text).removeprefix("Rp").replace(".", ""))

    rating = float(rating_el.text) if rating_el else 0.0

    creatorTuple = []
    if creatorContainer_el:
        creatorTuple = [child.text for child in creatorContainer_el.children]

    owner = creatorTuple[0] if len(creatorTuple) > 0 else None
    city = creatorTuple[1] if len(creatorTuple) > 1 else None

    product = ProductContainer(
        title=title,
        price=raw_price,
        rating=rating,
        owner=owner,
        city=city,
    )
    products.append(product)

filename = "products_results.csv"

df = pd.DataFrame([product.model_dump() for product in products])

df.to_csv("products_results.csv", index=False, sep=";", quoting=csv.QUOTE_ALL)
# finally:
#     driver.quit()
driver.quit()
