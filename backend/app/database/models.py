# Defines the database models for the application using SQLAlchemy ORM. 
# ach class represents a table in the database, with attributes corresponding to columns.
# Relationships between tables are also defined here.

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, ForeignKey

class Base(DeclarativeBase):
    pass

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)