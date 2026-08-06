# Endpoint for workouts generation/fetching

from fastapi import APIRouter
from app.services.generator import generate_workout
from app.schemas.workout import WorkoutResquest

# Used if the endpoint needs a session to the db
from app.database.db import SessionLocal 

router = APIRouter()

@router.post("/workout")
def get_workout(request: WorkoutResquest):

    workout = generate_workout(
        SessionLocal(),
        programDuration=request.programDuration,
        programDifficulty=request.programDifficulty,
        programGoal=request.programGoal,
        targetedMuscleGroups=request.targetedMuscleGroups,
        availableEquipments=request.availableEquipments
    )

    return {
        "exercises": workout
    }