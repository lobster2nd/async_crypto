import time

import aiohttp
import asyncio

from app.models import Ticker
from app.database import db_helper

async def fetch_price(session, currency):
    """Получение данных с биржи"""
    url = f"https://test.deribit.com/api/v2/public/get_index_price?index_name={currency}"
    async with session.get(url) as response:
        data = await response.json()
        return data['result']['index_price']


async def save_to_db(currency, price):
    """Сохранение данных в БД"""
    async for session in db_helper.get_db_session():
        ticker = Ticker(currency=currency,
                        price=price,
                        timestamp=int(time.time()))
        session.add(ticker)
        await session.commit()

async def get_prices():
    """Точка входа в программу"""
    async with aiohttp.ClientSession() as session:
        while True:
            btc_price = await fetch_price(session, 'btc_usd')
            eth_price = await fetch_price(session, 'eth_usd')

            await save_to_db('btc_usd', btc_price)
            await save_to_db('eth_usd', eth_price)
            await asyncio.sleep(60)
