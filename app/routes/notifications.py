from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import NotificationCreate, NotificationResponse
from app.crud import create_notification, get_notifications

router = APIRouter()

# Создание уведомления
@router.post("/", response_model=NotificationResponse)
async def create_new_notification(notification: NotificationCreate, db: AsyncSession = Depends(get_db)):
    return await create_notification(db, notification)

# Получение всех уведомлений
@router.get("/", response_model=list[NotificationResponse])
async def get_all_notifications(db: AsyncSession = Depends(get_db)):
    return await get_notifications(db)
