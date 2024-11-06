import time

import aiohttp
import asyncio

from app.database import session_factory, Ticker

async def fetch_price(session, currency):
    """Получение данных с биржи"""
    url = f"https://test.deribit.com/api/v2/public/get_index_price?index_name={currency}"
    async with session.get(url) as response:
        data = await response.json()
        return data['result']['index_price']


async def save_to_db(currency, price):
    """Сохранение данных в БД"""
    with session_factory() as session:
        ticker = Ticker(currency=currency,
                        price=price,
                        timestamp=int(time.time()))
        session.add(ticker)
        session.commit()

async def get_prices():
    """Точка входа в программу"""
    async with aiohttp.ClientSession() as session:
        while True:
            btc_price = await fetch_price(session, 'btc_usd')
            eth_price = await fetch_price(session, 'eth_usd')

            await save_to_db('btc_usd', btc_price)
            await save_to_db('eth_usd', eth_price)
            print(f"BTC/USD: {btc_price}, ETH/USD: {eth_price}")
            await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(get_prices())
