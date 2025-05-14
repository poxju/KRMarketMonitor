import asyncio
from scripts.scraper import fetch_all_prices
from scripts.utils import load_company_data
from scripts.priceMonitor import update_price_history, calculate_group_averages, check_conditions

async def monitor(interval, df, thresholds, sender_email, receiver_email, password):
    while True:
        print("Monitoring...")
        prices_dict = await fetch_all_prices(df['Company_Code'].tolist())
        print("Prices fetched. Prices dict: ", prices_dict)
        update_price_history(prices_dict)
        group_averages = calculate_group_averages(df, prices_dict)
        print("Group averages calculated. Group averages: ", group_averages)
        check_conditions(df, prices_dict, group_averages, thresholds, sender_email, receiver_email, password)
        print("Monitoring complete for this cycle.")
        await asyncio.sleep(interval)

if __name__ == "__main__":
    company_data = load_company_data('company_codes.xlsx')

    # Email configuration
    sender_email = "your_email@gmail.com"
    password = "your_password"
    receiver_email = "receiver_email@gmail.com"

    # Monitoring parameters
    thresholds = {
        'X1': 5,  # Percentage change for Condition 1
        'X2': 10,  # Percentage change for Condition 2
        'X3': 7,  # Percentage change for Condition 3
        'X4': 15,  # Percentage change for Condition 4
    }
    interval = 10  # Monitoring interval in seconds

    # Start monitoring
    asyncio.run(monitor(interval, company_data, thresholds, sender_email, receiver_email, password))