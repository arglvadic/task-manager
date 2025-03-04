from fastapi import FastAPI
from app.database import check_db_connection


app = FastAPI()

@app.get("/check-db")
async def check_db():
    await check_db_connection()
    return {"message": "База данных работает!"}

# Запуск проверки БД при старте сервера
@app.on_event("startup")
async def startup_event():
    await check_db_connection()
    print(" База данных проверена при старте сервера.")

# Uvicorn правильно запускает FastAPI, нет необходимости в asyncio.run()
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
