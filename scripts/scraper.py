from playwright.async_api import async_playwright
import re

async def fetch_all_prices(company_codes):
    prices = {}
    async with async_playwright() as p:
        # Launch the browser in headless mode
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        for code in company_codes:
            url = f"https://alphasquare.co.kr/home/stock-information?code={code}"
            try:
                await page.goto(url, timeout=20000)  # Set timeout to 20 seconds
                # Wait for the price element to load (adjust selector as needed)
                await page.wait_for_selector('h2.price-close', timeout=15000)  # 15 seconds timeout
                
                # Extract the price
                price_text = await page.inner_text('h2.price-close')
                print(f"Raw price text for {code}: {price_text}")
                
                # Remove any character that is not a digit or a decimal point
                # This will handle cases like '$228.51' as well as '$-'
                cleaned_price_text = re.sub(r'[^\d.-]+', '', price_text)
                
                if cleaned_price_text in ['', '-', None]:
                    print(f"Price unavailable for {code}.")
                    prices[code] = None
                else:
                    try:
                        price = float(cleaned_price_text)
                        prices[code] = price
                        print(f"Fetched price for {code}: {price}")
                    except ValueError:
                        print(f"Invalid price format for {code}: {cleaned_price_text}")
                        prices[code] = None
            except Exception as e:
                print(f"Error fetching price for {code}: {e}")
                prices[code] = None
        
        await browser.close()
    return prices