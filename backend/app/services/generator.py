# Contains functions for workout generation and manipulation

from app.database.db_functions import get_all_exercises

def generate_workout(db_session):
    exercises = get_all_exercises(db_session)
    workout = []

    for exercise in exercises:
        workout.append(exercise.name)

    return workout