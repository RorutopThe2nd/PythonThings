import asyncio

import playwright
import playwright.async_api


async def main():
    async with playwright.async_api.async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://the-internet.herokuapp.com/login")
        name_el = page.locator("#username")
        pass_el = page.locator("#password")

        await name_el.fill("tomsmith")
        await pass_el.fill("SuperSecretPassword!")

        await page.wait_for_timeout(5000)

        await page.locator('button[type="submit"]').click()

        await page.wait_for_timeout(30000)


asyncio.run(main())
