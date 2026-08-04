# Defines the schemas for workout data entering and leaving the API
# Allows API to send/receive specific data

from pydantic import BaseModel

class WorkoutResquest(BaseModel):
    programDuration: int
    programDifficulty: int
    programGoal: str
    targetedMuscleGroups: list[str]
    availableEquipments: list[str]