import asyncio
import csv
import json
import sys
import pandas as pd
from playwright.async_api import async_playwright
import os

from file_perm_check import file_perm_check

filename = "products_results.csv"

file_perm_check(filename)
url = "https://www.tokopedia.com/find/rtx-4060-laptop?utm_campaign=find&utm_medium=organic&utm_source=google"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            channel="chrome",
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--auto-open-devtools-for-tabs",
            ],
        )

        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 720},
        )

        page = await context.new_page()

        await page.goto(url, wait_until="domcontentloaded")

        await page.wait_for_function(
            "() => typeof window.__cache !== 'undefined' && window.__cache !== null"
        )
        # print(cache)

        # cache_json = await page.evaluate("() => JSON.stringify(window.__cache)")

        products = await page.evaluate("""
		() => {
			const cache = window.__cache;

			const targetKey = Object.keys(cache).find(k =>
				k.includes('searchProductV5') &&
				k.endsWith('.data')
			);

			if (!targetKey) return [];

			return cache[targetKey].products.map(ref => {
				const p = cache[ref.id];
				const price = cache[p.price.id]
				const shop = cache[p.shop.id]
								 
				return {
					name: p.name,
					price: price.text,
					url: p.url,
					shop: shop.name,
					city:shop.city
				
				};
			});
		}
		""")

        # for p in products[:20]:
        #     print(json.dumps(p, indent=2, ensure_ascii=False))

        df = pd.DataFrame(products)

        df.to_csv(filename, index=False, sep=";", quoting=csv.QUOTE_ALL)

        await browser.close()


asyncio.run(main())
