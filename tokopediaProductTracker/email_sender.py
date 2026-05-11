import base64
import os
import resend
from dotenv import load_dotenv

from tokopediaProductTracker.price_formatter import format_price

load_dotenv()

resend.api_key = os.getenv("RESEND_API")


def send_email(product_name: str, new_price: int, last_price: int):
    r = resend.Emails.send(
        {
            "from": "onboarding@resend.dev",
            "to": os.getenv("EMAIL"),  # type: ignore
            "subject": f"🚨 Price Drop Alert: {product_name}",
            "html": f"<p>Good news! The price dropped from {format_price(last_price)} to {format_price(new_price)}!</p>",
        }
    )
