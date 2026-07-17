# Contains functions for workout generation and manipulation

from app.database.db_functions import get_all_exercises

def generate_workout(db_session, programDuration = 60, programDifficulty = 3, programGoal = "No particular goal", targetedMuscleGroups = ["Everything"], availableEquipments = ["Everything"]):
    workout = []
    activation = ...
    
    exercises = get_all_exercises(db_session)

    for exercise in exercises:
        workout.append(exercise.name)

    return workout