# Contains functions for workout generation and manipulation

from app.database.db_functions import get_all_exercises, get_random_exercises

def generate_workout(db_session, programDuration = 60, programDifficulty = 3, programGoal = "No particular goal", targetedMuscleGroups = ["Everything"], availableEquipments = ["Everything"]):
    workout = []
    

    match programDuration:
        case 45, 60:
            activation_p = get_random_exercises(db_session, count=2, experienceLevel = programDifficulty, difficultyLevel = 5, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "main", availableEquipments = availableEquipments)
            main_p = get_random_exercises(db_session, count=2, experienceLevel = programDifficulty, difficultyLevel = 7, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "secondary", availableEquipments = availableEquipments)
            finisher_p = get_random_exercises(db_session, count=1, experienceLevel = programDifficulty, difficultyLevel = 5, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "main", availableEquipments = availableEquipments)
        case 75, 90:
            pass
        case 105, 120:
            pass
    
    for exercise in activation_p:
        exo = {
            "name": exercise.name,
            "description": exercise.description,
            "equipment": exercise.requiredEquipments,
            "series": 3,
            "repetitions": round((10 - exercise.difficultyLevel) * 1.5),
            "rest": 60
        }
        workout.append(exo)

    return workout