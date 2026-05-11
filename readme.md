# Python Things

Welcome to my python things branch! In this repository I showcase one of my examples of what I can do!

## ⚙️ To use it

```bash
git clone https://github.com/RorutopThe2nd/PythonThings
pip install -r requirements.txt
```

Create a .env file in the root directory and add your credentials:

```env
RESEND_API=your_resend_api_key_here
EMAIL=your_email@example.com
```

## 🏷️ Tokopedia Product Price Tracker

An automated Python tool that tracks product prices on Tokopedia, logs the history in a local database, and sends an email alert if the price drops.

Instead of using a slow browser simulator, this script directly queries Tokopedia's hidden GraphQL API for lightning-fast and reliable results.

### ✨ Key Features

- Direct API Extraction: Intercepts and uses Tokopedia's internal GraphQL API instead of traditional web scraping, making it extremely fast and lightweight.
- Price Drop Alerts: Automatically sends an email notification via the Resend API if a product's price goes down.
- Historical Logging: Saves price history to a local SQLite database using Peewee ORM.
- Data Validation: Uses Pydantic to ensure the scraped data is cleanly structured and type-safe.
- Smart Tracking: Only logs new data when the price changes, keeping the database clean.

### 🛠️ Tech Stack

- Language: Python (Asyncio)
- Data Extraction: requests (GraphQL API Interception)
- Database: SQLite via Peewee ORM
- Data Validation: Pydantic
- Email Alerts: Resend API
- Environment Management: python-dotenv

### ⚙️ Run the Tracker

```bash
python -m tokopediaProductTracker
```

### 🖥️ Example Output

When the price hasn't changed:

```text
Product Price is still the same. Product Price: Rp16,567,000.00 == Last Price: Rp16,567,000.00
```

When the price drops:

```text
Product Price Log is set! Data: {'name': 'Colorful EVOL P15...', 'price': 15567000}
Product Price WENT DOWN! Sending email now! Product Price: Rp15,567,000.00 < Last Price: Rp16,567,000.00
```
