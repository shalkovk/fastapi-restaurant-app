from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncConnection, async_sessionmaker, AsyncSession, create_async_engine

from src.config import settings

engine = create_async_engine(url=settings.DB_URL)

async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, autocommit=False, autoflush=False, expire_on_commit=False)


async def get_async_connection() -> AsyncGenerator[AsyncConnection, None]:
    async with engine.begin() as conn:
        yield conn


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
