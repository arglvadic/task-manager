from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User, Task, Event, Notification
from app.schemas import UserCreate, TaskCreate, EventCreate, NotificationCreate

# Создание пользователя
async def create_user(db: AsyncSession, user: UserCreate):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

# Получение всех пользователей
async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

# Создание задачи
async def create_task(db: AsyncSession, task: TaskCreate):
    new_task = Task(title=task.title, description=task.description, assignee_id=task.assignee_id)
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

# Получение всех задач
async def get_tasks(db: AsyncSession):
    result = await db.execute(select(Task))
    return result.scalars().all()

# Создание события
async def create_event(db: AsyncSession, event: EventCreate):
    new_event = Event(event_type=event.event_type, payload=event.payload,
                      users_id=event.users_id, tasks_id=event.tasks_id, notifications_id=event.notifications_id)
    db.add(new_event)
    await db.commit()
    await db.refresh(new_event)
    return new_event

# Получение всех событий
async def get_events(db: AsyncSession):
    result = await db.execute(select(Event))
    return result.scalars().all()

# Создание уведомления
async def create_notification(db: AsyncSession, notification: NotificationCreate):
    new_notification = Notification(users_id=notification.users_id, tasks_id=notification.tasks_id, message=notification.message)
    db.add(new_notification)
    await db.commit()
    await db.refresh(new_notification)
    return new_notification

# Получение всех уведомлений
async def get_notifications(db: AsyncSession):
    result = await db.execute(select(Notification))
    return result.scalars().all()

