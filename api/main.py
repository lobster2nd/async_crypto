import asyncio

from fastapi import FastAPI
from contextlib import asynccontextmanager

import uvicorn

from app.models import Base
from app.database import db_helper
from api.views import router as ticker_router
from app.utils import get_prices


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    task = asyncio.create_task(get_prices())

    yield

    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        pass


app = FastAPI(lifespan=lifespan)
app.include_router(ticker_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
