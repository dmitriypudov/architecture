from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
import secrets  # Добавляем импорт

Base = declarative_base()

class URL(Base):
    __tablename__ = "urls"
    
    short_code = Column(String, primary_key=True)
    long_url = Column(String)
    
    @staticmethod
    def generate_short_code():
        return secrets.token_urlsafe(5)[:6]  # Генерация кода