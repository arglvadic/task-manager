from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Схема для создания пользователя
class UserCreate(BaseModel):
    name: str
    email: EmailStr

# Схема ответа для пользователя
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True  # Позволяет преобразовывать SQLAlchemy-модель в Pydantic

# Схема для создания задачи
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    assignee_id: Optional[int] = None

# Схема ответа для задачи
class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    assignee_id: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True

# Схема для создания события (event)
class EventCreate(BaseModel):
    event_type: str
    payload: dict
    users_id: Optional[int] = None
    tasks_id: Optional[int] = None
    notifications_id: Optional[int] = None

# Схема ответа для события
class EventResponse(BaseModel):
    id: int
    event_type: str
    payload: dict
    users_id: Optional[int]
    tasks_id: Optional[int]
    notifications_id: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True

# Схема для создания уведомления
class NotificationCreate(BaseModel):
    users_id: int
    tasks_id: Optional[int] = None
    message: str

# Схема ответа для уведомления
class NotificationResponse(BaseModel):
    id: int
    users_id: int
    tasks_id: Optional[int]
    message: str
    sent_at: datetime

    class Config:
        from_attributes = True
