# Endpoint for workouts generation/fetching

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.services.generator import generate_workout
from app.services.pdf_generator import generate_workout_pdf
from app.schemas.workout import WorkoutRequest, PdfRequest

# Used if the endpoint needs a session to the db
from app.database.db import SessionLocal 

router = APIRouter()

@router.post("/workout")
def get_workout(request: WorkoutRequest):

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

@router.post("/workout/pdf")
def download_workout_pdf(request: PdfRequest):

    pdf = generate_workout_pdf(request.workout, request.pdfFilters)

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=workout.pdf"}
    )