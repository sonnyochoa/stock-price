import asyncio
import aiohttp
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class StockPriceMonitor:
    def __init__(self, symbols, api_key):
        self.symbols = symbols
        self.api_key = api_key
        self.prices = {symbol: None for symbol in symbols}
        self.alerts = []

    async def fetch_price(self, session, symbol):
        url = f"https://api.tiingo.com/tiingo/daily/{symbol}/prices"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Token {self.api_key}'
        }
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            return symbol, float(data[0]['close'])

    async def monitor_prices(self):
        async with aiohttp.ClientSession() as session:
            while True:
                tasks = [self.fetch_price(session, symbol) for symbol in self.symbols]
                results = await asyncio.gather(*tasks)
                
                for symbol, price in results:
                    if self.prices[symbol] is not None:
                        change = (price - self.prices[symbol]) / self.prices[symbol]
                        if abs(change) > 0.01:  # 1% change
                            self.alerts.append(f"Alert: {symbol} price changed by {change:.2%}")
                    
                    self.prices[symbol] = price
                
                print(json.dumps(self.prices, indent=2))
                if self.alerts:
                    print("\nAlerts:")
                    for alert in self.alerts:
                        print(alert)
                    self.alerts.clear()
                
                await asyncio.sleep(60)  # Wait for 1 minute before next update

async def main():
    symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
    api_key = os.environ.get('TIINGO_API_KEY')
    if not api_key:
        raise ValueError("TIINGO_API_KEY not found in .env file")
    monitor = StockPriceMonitor(symbols, api_key)
    await monitor.monitor_prices()

if __name__ == "__main__":
    asyncio.run(main())