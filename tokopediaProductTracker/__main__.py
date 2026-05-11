import asyncio
from datetime import datetime

from tokopediaProductTracker.database import (
    get_last_price,
    initialize_db,
    set_price_history,
)
from tokopediaProductTracker.email_sender import send_email
from tokopediaProductTracker.price_formatter import format_price
from tokopediaProductTracker.price_request import request_product_data


async def main():
    initialize_db()
    product_data = await request_product_data()

    last_price = get_last_price(product_data.name)

    price_formatted = format_price(product_data.price)
    if last_price is not None and last_price == product_data.price:
        print(
            "Product Price is still the same.",
            f"Product Price: {price_formatted} == Last Price: {format_price(last_price)}",
        )
    else:
        print("Product Price Log is set! Data:", product_data.model_dump())
        print(datetime.now())
        set_price_history(product_data.name, product_data.price)

        if last_price is not None:
            last_price_formatted = format_price(last_price)
            if product_data.price < last_price:
                print(
                    "Product Price WENT DOWN! Sending email now!",
                    f"Product Price: {price_formatted} < Last Price: {last_price_formatted}",
                )
                send_email(product_data.name, product_data.price, last_price)
            else:
                print("Last Price:", {last_price_formatted})


# print(await request_product_data())


if __name__ == "__main__":
    asyncio.run(main())
