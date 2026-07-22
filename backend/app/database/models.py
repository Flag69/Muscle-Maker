# Defines the database models for the application using SQLAlchemy ORM. 
# ach class represents a table in the database, with attributes corresponding to columns.
# Relationships between tables are also defined here.

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, ForeignKey, JSON

class Base(DeclarativeBase):
    pass


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)
    experienceLevel = Column(Integer, nullable=True) # 1 to 4, user's experience level
    difficultyLevel = Column(Integer, nullable=True) # 1 to 10, exercise's difficulty level
    primaryMuscles = Column(JSON, nullable=True)
    secondaryMuscles = Column(JSON, nullable=True)
    requiredEquipments = Column(JSON, nullable=True)
    defaultReps = Column(Integer, nullable=True)
    defaultSets = Column(Integer, nullable=True)
    defaultRest = Column(Integer, nullable=True) # in seconds