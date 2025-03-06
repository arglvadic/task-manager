from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas import TaskCreate, TaskResponse
from app.crud import create_task, get_tasks

router = APIRouter()

# Создание новой задачи
@router.post("/", response_model=TaskResponse)
async def create_new_task(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await create_task(db, task)

# Получение всех задач
@router.get("/", response_model=list[TaskResponse])
async def get_all_tasks(db: AsyncSession = Depends(get_db)):
    return await get_tasks(db)
