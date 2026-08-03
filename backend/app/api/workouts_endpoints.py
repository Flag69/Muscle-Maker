# Endpoint for workouts generation/fetching

from fastapi import APIRouter
from app.services.generator import generate_workout

# Used if the endpoint needs a session to the db
from app.database.db import SessionLocal 

router = APIRouter()

@router.get("/workout")
def get_workout():

    workout = generate_workout(SessionLocal(), programDuration=60, programDifficulty=3, programGoal="strength", targetedMuscleGroups=["Chest", "Back"], availableEquipments=["Dumbbell", "Barbell"])
    
    return {
        "exercises": workout
    }