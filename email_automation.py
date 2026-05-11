import base64
import os
import resend
from dotenv import load_dotenv

load_dotenv()


resend.api_key = os.getenv("RESEND_API")

file_path = "bitcoin_prices_log.csv"
with open(file_path, "rb") as f:
    csv_content = base64.b64encode(f.read()).decode("utf-8")

r = resend.Emails.send(
    {
        "from": "onboarding@resend.dev",
        "to": os.getenv("EMAIL"),  # type: ignore
        "subject": "Bitcoin Log Report",
        "html": "<p>Your bitcoin prices log today is ready!</p>",
        "attachments": [{"filename": file_path, "content": csv_content}],
    }
)
