# Initializes the database connection

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.models import Base

DATABASE_URL = "sqlite:///gym.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)