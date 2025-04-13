from src.config import settings
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_async_engine(url=settings.get_database_url)

async_session_factory = sessionmaker(
    engine,
    class_= AsyncSession,
    expire_on_commit = False,
)


class Base(DeclarativeBase): ...
