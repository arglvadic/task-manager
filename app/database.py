from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text  #Используем text() для выполнения SQL-запросов

from app.config import settings


#Создаём асинхронный движок SQLAlchemy
engine = create_async_engine(settings.DATABASE_URL)

#Создаём асинхронную сессию
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

#Базовый класс для моделей
class Base(DeclarativeBase):
    pass

#Функция проверки подключения к БД
async def check_db_connection():
    try:
        async with engine.begin() as conn:
            await conn.execute(text("SELECT 1"))  #Используем text() для корректного SQL-запроса
        print(" Подключение к базе данных успешно!")
    except OperationalError as e:
        print(" Ошибка подключения к базе:", e)

