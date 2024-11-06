from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column


Base = declarative_base()

class Ticker(Base):
    __tablename__ = "tickers"

    id: Mapped[int] = mapped_column(primary_key=True)
    currency: Mapped[str]
    price: Mapped[float]
    timestamp: Mapped[int]

DATABASE_URL = "sqlite:///tickers.db"
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)

session_factory = sessionmaker(bind=engine)
