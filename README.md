# Stock Price Monitor

This project is a real-time stock price monitoring system built with Python. It uses asyncio for efficient handling of concurrent API requests and provides alerts for significant price changes.

## Features

- Real-time monitoring of multiple stock symbols
- Asynchronous API requests for improved performance
- Price change alerts (currently set at 1% change threshold)
- Uses Tiingo API for fetching stock price data

## Requirements

- Python 3.7+
- aiohttp
- python-dotenv

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/sonnyochoa/stock-price.git
   cd stock-price
   ```

2. Install the required packages:
   ```
   pip install aiohttp python-dotenv
   ```

3. Create a `.env` file in the project root and add your Tiingo API key:
   ```
   TIINGO_API_KEY=your_api_key_here
   ```

4. (Optional) Modify the list of stock symbols in `main.py` if desired.

## Usage

Run the script with:

```
python main.py
```

The program will start monitoring the specified stock symbols and print updates every minute. It will also display alerts for any price changes greater than 1%.

## Code Structure

- `StockPriceMonitor` class: Manages the monitoring of stock prices.
  - `__init__`: Initializes the monitor with a list of stock symbols.
  - `fetch_price`: Asynchronously fetches the price for a single stock symbol.
  - `monitor_prices`: Continuously monitors prices for all symbols and generates alerts.

- `main` function: Sets up and runs the stock price monitor.

## Customization

- To change the monitored symbols, modify the `symbols` list in the `main` function.
- To adjust the alert threshold, change the condition in the `monitor_prices` method (currently set to `abs(change) > 0.01` for 1% change).

## Note

This project uses environment variables to securely manage API keys. Make sure to keep your `.env` file private and never commit it to version control.

## License

[MIT License](https://opensource.org/licenses/MIT)

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/sonnyochoa/stock-price/issues) if you want to contribute.