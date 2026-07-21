# Contains functions to query the database

import random

from app.database.models import Exercise

def create_exercise(db_session, name):
    new_exercise = Exercise(name=name)
    db_session.add(new_exercise)
    db_session.commit()
    db_session.refresh(new_exercise)
    return new_exercise

def get_all_exercises(db_session):
    return db_session.query(Exercise).all()

# Get random exercises based on different criterias
def get_random_exercises(db_session, count=1, experienceLevel = 4, difficultyLevel = 10, targetedMuscleGroups = None, targetedMuscleType = "main", availableEquipments = None):
    query = db_session.query(Exercise)

    if experienceLevel:
        query = query.filter(Exercise.experienceLevel <= experienceLevel)
    if difficultyLevel:
        query = query.filter(Exercise.difficultyLevel <= difficultyLevel)

    exercises = query.all()

    filtered_exercises = []
    available_equipment_set = (set(availableEquipments) if availableEquipments else None)
    for exercise in exercises:

        match targetedMuscleType:
            case "main":
                if targetedMuscleGroups and exercise.primaryMuscles not in targetedMuscleGroups:
                    continue
            case "secondary":
                if targetedMuscleGroups and exercise.secondaryMuscles not in targetedMuscleGroups:
                    continue
        if available_equipment_set:
            if not set(exercise.requiredEquipments).issubset(available_equipment_set):
                continue
        filtered_exercises.append(exercise)

    selected_exercises = random.sample(filtered_exercises, min(count, len(filtered_exercises)))

    return selected_exercises
