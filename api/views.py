from datetime import datetime

from fastapi import APIRouter, Query, HTTPException
from sqlalchemy import select, desc, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app import db_helper, Ticker

router = APIRouter(prefix="/tickers")


@router.get("/")
async def get_tickers(ticker: str = Query(..., example='btc_usd')):
    """Получение всех сохраненных данных по указанной валюте"""
    session: AsyncSession = await db_helper.get_session()
    async with session:
        result = await session.execute(select(Ticker)
                                       .filter(Ticker.currency == ticker))
        tickers = result.scalars().all()

        if not tickers:
            raise HTTPException(status_code=404,
                                detail="Ничего не найдено")

        return tickers


@router.get("/latest/")
async def get_latest_ticker(ticker: str = Query(...,
                                                example='btc_usd')):
    """Получение последней сохранённой цены указанной валюты"""
    session: AsyncSession = await db_helper.get_session()
    async with session:
        result = await session.execute(
            select(Ticker)
            .filter(Ticker.currency == ticker)
            .order_by(desc(Ticker.timestamp))
            .limit(1)
        )
        latest_ticker = result.scalars().first()

        if not latest_ticker:
            raise HTTPException(status_code=404,
                                detail="Ничего не найдено")

        return latest_ticker


@router.get("/by_date/")
async def get_tickers_by_date(
    ticker: str = Query(..., example='btc_usd'),
    start_date: str = Query(..., description='формат YYYY-MM-DD',
                            example='2020-01-01'),
    end_date: str = Query(..., description='формат YYYY-MM-DD',
                            example='2020-01-01')):
    """Получение цен по указанной валюте по дате в формате 'YYYY-MM-DD'"""

    try:
        start_date = int(datetime.fromisoformat(start_date).timestamp())
        end_date = int(datetime.fromisoformat(end_date).timestamp())
    except ValueError:
        raise HTTPException(status_code=400, detail="Неверный формат даты")

    session: AsyncSession = await db_helper.get_session()
    async with session:
        result = await session.execute(
            select(Ticker)
            .filter(
                Ticker.currency == ticker,
                and_(Ticker.timestamp >= start_date,
                     Ticker.timestamp <= end_date
                )
            )
        )
        tickers = result.scalars().all()

        if not tickers:
            raise HTTPException(status_code=404, detail="Ничего не найдено")

        return tickers
