# Endpoints for exercises generation/fetching

from fastapi import APIRouter
from app.services.generator import generate_workout

# Used if the endpoint needs a session to the db
from app.database.db import SessionLocal 

router = APIRouter()

@router.get("/exercises")
def get_exercices():
    return {"exercises": [
        {"name": "Push-ups", "description": "A bodyweight exercise that targets the chest, shoulders, and triceps."},
        {"name": "Squats", "description": "A lower body exercise that targets the quadriceps, hamstrings, and glutes."},
        {"name": "Pull-ups", "description": "An upper body exercise that targets the back, shoulders, and biceps."}
    ]}