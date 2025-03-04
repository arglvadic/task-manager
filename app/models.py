from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func


class Task(Base):
    __tablename__  = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Уникальный ID задачи
    description = Column(String, nullable=False)  # Описание задачи
    status = Column(String, default="pending")  # Статус (например, "pending", "in_progress", "done")
    priority = Column(String, nullable=False)  # Приоритет (low, medium, high)
    deadline = Column(DateTime, nullable=True)  # Дата дедлайна
    #assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # ID пользователя-исполнителя
    created_at = Column(DateTime, default=func.now())  # Дата создания
