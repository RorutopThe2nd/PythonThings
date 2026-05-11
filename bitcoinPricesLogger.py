from datetime import datetime
import os

import pandas as pd
import requests


priceRequest = requests.get(
    "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
)

priceJson = priceRequest.json()
usd = priceJson["bitcoin"]["usd"]

formatted_ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

filename = "bitcoin_prices_log.csv"

file_exists = os.path.isfile(filename)

df = pd.DataFrame({"Bitcoin Price in USD": [usd], "Timestamp": [formatted_ts]})

df.to_csv(filename, index=False, mode="a", header=not file_exists)
