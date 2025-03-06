from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import EventCreate, EventResponse
from app.crud import create_event, get_events

router = APIRouter()

# Запись события
@router.post("/", response_model=EventResponse)
async def create_new_event(event: EventCreate, db: AsyncSession = Depends(get_db)):
    return await create_event(db, event)

# Получение всех событий
@router.get("/", response_model=list[EventResponse])
async def get_all_events(db: AsyncSession = Depends(get_db)):
    return await get_events(db)
