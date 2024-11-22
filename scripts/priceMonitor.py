from collections import defaultdict
from scripts.notification import send_email

price_history = defaultdict(list)

def update_price_history(prices):
    for code, price in prices.items():
        if price is not None:
            price_history[code].append(price)
            if len(price_history[code]) > 10:  # Limit history size
                price_history[code].pop(0)

def calculate_group_averages(df, prices):
    df['Price'] = [prices.get(code) for code in df['Company_Code']]
    group_averages = df.groupby('Group')['Price'].mean().to_dict()
    return group_averages

def check_conditions(df, prices, group_averages, thresholds, sender_email, receiver_email, password):
    for code, price in prices.items():
        if price is None or len(price_history[code]) < 2 or price_history[code][-1] is None:
            continue  # Skip this iteration if data is invalid
        # Condition 1: Current price > previous price * (1 + X1%)
        if price > price_history[code][-1] * (1 + thresholds['X1'] / 100):
            send_email(
                f"Stock Alert: {code}",
                f"The price for {code} has exceeded the X1 threshold.",
                sender_email,
                receiver_email,
                password,
            )
        # Add conditions for group averages here
        group = df.loc[df['Company_Code'] == code, 'Group'].iloc[0]
        if group_averages.get(group) is not None and group_averages[group] > thresholds['X3']:
            send_email(
                f"Group Alert: Group {group}",
                f"The average price of Group {group} has exceeded the threshold.",
                sender_email,
                receiver_email,
                password,
            )