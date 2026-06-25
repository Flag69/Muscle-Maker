# Endpoints for exercises generation/fetching

from fastapi import APIRouter
from app.services.generator import generate_workout

# Used if the endpoint needs a session to the db
from app.database.db import SessionLocal 

router = APIRouter()

@router.get("/exercises")
def get_exercices():
    return {"exercises": "squat lol"}