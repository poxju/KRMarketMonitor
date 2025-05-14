# Korean Stock Market Monitor

This project monitors the prices of Korean stocks, calculates group averages, checks for specific conditions, and sends email notifications when thresholds are met.

## Features

- Fetches real-time prices for a list of companies.
- Calculates group averages for stock prices.
- Checks for customizable conditions based on percentage changes.
- Sends email alerts when conditions are met.
- Runs continuously at a user-defined interval.

## Requirements

- Python 3.8+
- `pandas`
- `asyncio`
- Other dependencies as required by `scripts/`

## Setup

1. **Clone the repository**  
   ```
   git clone <repo-url>
   cd Korean-Stock-Market-Monitor
   ```

2. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

3. **Prepare company data**  
   - Place your `company_codes.xlsx` file in the project root.
   - The file should contain a column named `Company_Code` with the stock codes.

4. **Configure email settings**  
   - Edit `main.py` and set your Gmail address, password, and receiver email:
     ```python
     sender_email = "your_email@gmail.com"
     password = "your_password"
     receiver_email = "receiver_email@gmail.com"
     ```
   - For Gmail, you may need to use an App Password.

5. **Set monitoring thresholds and interval**  
   - Adjust the `thresholds` dictionary and `interval` variable in `main.py` as needed.

## Usage

Run the monitor script:

```
python main.py
```

The script will:
- Load company codes from `company_codes.xlsx`
- Start monitoring prices at the specified interval
- Print status updates to the console
- Send email notifications when conditions are met

## Customization

- Modify `scripts/priceMonitor.py` to change how group averages or conditions are calculated.
- Update `scripts/scraper.py` to change how prices are fetched.

## Notes

- Ensure your email credentials are kept secure.
- This script is for educational and informational purposes.
