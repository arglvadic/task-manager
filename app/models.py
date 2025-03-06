from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

# Таблица пользователей
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)  # Уникальный ID
    name = Column(String, nullable=False)  # Имя пользователя
    email = Column(String, unique=True, nullable=False)  # Почта, должна быть уникальной
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Дата создания пользователя

    # Связи с другими таблицами
    tasks = relationship("Task", back_populates="assignee")  # Пользователь может иметь несколько задач
    notifications = relationship("Notification", back_populates="user")  # Уведомления, связанные с пользователем
    events = relationship("Event", back_populates="user")  # Лог событий, связанных с пользователем


# Таблица задач
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)  # Уникальный ID задачи
    title = Column(String, nullable=False)  # Название задачи
    description = Column(Text, nullable=True)  # Описание задачи (может быть пустым)
    assignee_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # Кто отвечает за выполнение задачи
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Дата создания задачи

    # Связи
    assignee = relationship("User", back_populates="tasks")  # Связь с пользователем, который отвечает за задачу
    notifications = relationship("Notification", back_populates="task")  # Уведомления, связанные с задачей
    events = relationship("Event", back_populates="task")  # Лог событий для этой задачи


# Таблица событий (используется для логирования изменений, например, через Kafka)
class Event(Base):
    __tablename__ = "events.py"

    id = Column(Integer, primary_key=True, index=True)  # Уникальный ID события
    event_type = Column(String, nullable=False)  # Тип события (например, "task_created" или "task_completed")
    payload = Column(JSON, nullable=False)  # Данные события в формате JSON
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Дата и время события

    # Внешние ключи для связи с другими таблицами
    users_id = Column(Integer, ForeignKey("users.id"))  # ID пользователя, связанного с событием
    tasks_id = Column(Integer, ForeignKey("tasks.id"))  # ID задачи, связанной с событием
    notifications_id = Column(Integer, ForeignKey("notifications.id"))  # ID уведомления, связанного с событием

    # Связи
    user = relationship("User", back_populates="events.py")  # Лог событий пользователя
    task = relationship("Task", back_populates="events.py")  # Лог событий задачи
    notification = relationship("Notification", back_populates="events.py")  # Лог событий уведомлений


# Таблица уведомлений (например, для отправки e-mail или сообщений в чат)
class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)  # Уникальный ID уведомления
    users_id = Column(Integer, ForeignKey("users.id"))  # Кому отправлено уведомление
    tasks_id = Column(Integer, ForeignKey("tasks.id"))  # По какой задаче уведомление
    message = Column(Text, nullable=False)  # Текст уведомления
    sent_at = Column(DateTime(timezone=True), server_default=func.now())  # Когда уведомление было отправлено

    # Связи
    user = relationship("User", back_populates="notifications")  # Уведомления пользователя
    task = relationship("Task", back_populates="notifications")  # Уведомления задачи
    events = relationship("Event", back_populates="notification")  # Лог событий по уведомлению