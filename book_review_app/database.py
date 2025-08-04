from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "sqlite:///books.db"  # Archivo local, puedes cambiar a PostgreSQL si deseas

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
