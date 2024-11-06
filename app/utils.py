import aiohttp
import asyncio

async def fetch_price(session, currency):
    url = f"https://test.deribit.com/api/v2/public/get_index_price?index_name={currency}"
    async with session.get(url) as response:
        data = await response.json()
        return data['result']['index_price']

async def get_prices():
    async with aiohttp.ClientSession() as session:
        while True:
            btc_price = await fetch_price(session, 'btc_usd')
            eth_price = await fetch_price(session, 'eth_usd')
            print(f"BTC/USD: {btc_price}, ETH/USD: {eth_price}")
            await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(get_prices())
