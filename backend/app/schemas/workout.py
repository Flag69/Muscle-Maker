# Defines the schemas for workout data entering and leaving the API
# Allows API to send/receive specific data

from pydantic import BaseModel

class WorkoutRequest(BaseModel):
    programDuration: int
    programDifficulty: int
    programGoal: str
    targetedMuscleGroups: list[str]
    availableEquipments: list[str]

class WorkoutExercise(BaseModel):
    Name: str
    Description: str
    Sets: int
    Reps: int
    RepsType: str
    Rest: int

class GeneratedWorkout(BaseModel):
    exercises: list[WorkoutExercise]