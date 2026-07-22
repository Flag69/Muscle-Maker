# Contains functions for workout generation and manipulation

from app.database.db_functions import get_all_exercises, get_random_exercises

def generate_workout(db_session, programDuration = 60, programDifficulty = 3, programGoal = None, targetedMuscleGroups = None, availableEquipments = None):
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

    return workout

def add_exercises_to_workout(workout, exercises, programPart, programGoal):
    for exercise in exercises:
        exo = {
            "Name": exercise.name,
            "Description": exercise.description
        }


        workout.append(exo)
    return workout

def get_program_params(programPart, programGoal):
    setsMult, repsMult, restMult = 1, 1, 1
    params = TRAINING_PARAMETERS.get(programPart, {}).get(programGoal, {})
    setsMult = params.get("setsMult", 1)
    repsMult = params.get("repsMult", 1)
    restMult = params.get("restMult", 1)

    return setsMult, repsMult, restMult

TRAINING_PARAMETERS = {
    "activation_p": {
        "strength": {"setsMult": 2, "repsMult": 1, "restMult": 1.5},
        "hypertrophy": {"setsMult": 1, "repsMult": 1.5, "restMult": 1},
        "endurance": {"setsMult": 1, "repsMult": 2, "restMult": 1},
    },
    "main_p": {
        "strength": {"setsMult": 5, "repsMult": 5, "restMult": 180},
        "hypertrophy": {"setsMult": 4, "repsMult": 8, "restMult": 120},
        "endurance": {"setsMult": 3, "repsMult": 15, "restMult": 60},
    },
    "accessory_p": {
        "strength": {"setsMult": 3, "repsMult": 10, "restMult": 90},
        "hypertrophy": {"setsMult": 3, "repsMult": 12, "restMult": 90},
        "endurance": {"setsMult": 2, "repsMult": 15, "restMult": 60},
    },
    "finisher_p": {
        "strength": {"setsMult": 2, "repsMult": 10, "restMult": 60},
        "hypertrophy": {"setsMult": 2, "repsMult": 12, "restMult": 60},
        "endurance": {"setsMult": 2, "repsMult": 15, "restMult": 45},
    },
}