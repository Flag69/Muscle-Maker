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
def get_random_exercises(db_session, count=1, experienceLevel = 4, difficultyLevel = 10, targetedMuscleGroups = None, targetedMuscleType = "main", availableEquipments = None, exercisesToExclude = None):
    query = db_session.query(Exercise)

    if exercisesToExclude:
        excluded_id = []

        for exercise in exercisesToExclude:
            excluded_id.append(exercise.id)

        query = query.filter(Exercise.id.notin_(excluded_id))

    if experienceLevel:
        query = query.filter(Exercise.experienceLevel <= experienceLevel)
    if difficultyLevel:
        query = query.filter(Exercise.difficultyLevel <= difficultyLevel)

    exercises = query.all()

    filtered_exercises = []

    for exercise in exercises:

        if targetedMuscleGroups != None and targetedMuscleGroups != ["Everything"]:
            match targetedMuscleType:
                case "main":
                    muscleIsTargeted = False
                    for muscle in targetedMuscleGroups:
                        if muscle in exercise.primaryMuscles:
                            muscleIsTargeted = True
                            break
                    if not muscleIsTargeted:
                        continue

                case "secondary":
                    muscleIsTargeted = False
                    for muscle in targetedMuscleGroups:
                        if muscle in exercise.secondaryMuscles:
                            muscleIsTargeted = True
                            break
                    if not muscleIsTargeted:
                        continue
                    # TODO : Add a case for "any" targetedMuscleType if needed

        if availableEquipments != None and availableEquipments != ["Everything"]:
            if availableEquipments == ["Nothing (bodyweight only)"] and exercise.requiredEquipments != []:
                continue
            else:
                if not set(exercise.requiredEquipments).issubset(set(availableEquipments)):
                    continue

        filtered_exercises.append(exercise)


    selected_exercises = random.sample(filtered_exercises, min(count, len(filtered_exercises)))

    return selected_exercises
