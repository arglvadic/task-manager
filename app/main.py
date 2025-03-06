from fastapi import FastAPI
from app.database import engine, Base
from app.routes import users ,tasks, events , notifications

# Создаём объект FastAPI
app = FastAPI(title="Task Manager API", version="1.0")

# Подключаем маршруты API
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])
app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])

# Корневой эндпоинт (для проверки работы сервера)
@app.get("/")
async def root():
    return {"message": "Task Manager API is running"}

# Функция для инициализации БД (создание таблиц)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Запуск сервера (если файл запускается напрямую)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
