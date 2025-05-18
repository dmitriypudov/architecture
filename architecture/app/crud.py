from fastapi import HTTPException
from fastapi.responses import RedirectResponse  # Добавляем импорт
from sqlalchemy.orm import Session
from .models import URL, Base  # Импортируем модели
from fastapi import FastAPI
from app.database import SessionLocal  # Импортируем сессию

app = FastAPI()  # Если используешь FastAPI в этом файле

# Инициализация БД (если нужно)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Пример CRUD-операции
def create_url(db: Session, long_url: str):
    short_code = URL.generate_short_code()
    db_url = URL(short_code=short_code, long_url=long_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url(db: Session, short_code: str):
    url = db.query(URL).filter(URL.short_code == short_code).first()
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    return url