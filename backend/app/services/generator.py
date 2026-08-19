# Contains functions for workout generation and manipulation

from random import randint, randrange

from app.database.db_functions import get_all_exercises, get_random_exercises

def generate_workout(db_session, programDuration = 60, programDifficulty = 3, programGoal = None, targetedMuscleGroups = None, availableEquipments = None):
    workout = []
    exercises_to_exclude = []
    

    match programDuration:
        case 45 | 60:
            warm_up_p = get_random_exercises(db_session, count=1, experienceLevel = programDifficulty, difficultyLevel = 3, targetedMuscleGroups = ["Cardiovascular system"], targetedMuscleType = "main", availableEquipments = availableEquipments, exercisesToExclude=exercises_to_exclude)
            exercises_to_exclude.extend(warm_up_p)
            activation_p = get_random_exercises(db_session, count=2, experienceLevel = programDifficulty, difficultyLevel = 5, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "secondary", availableEquipments = availableEquipments, exercisesToExclude=exercises_to_exclude)
            exercises_to_exclude.extend(activation_p)
            main_p = get_random_exercises(db_session, count=2, experienceLevel = programDifficulty, difficultyLevel = 7, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "main", availableEquipments = availableEquipments, exercisesToExclude=exercises_to_exclude)
            exercises_to_exclude.extend(main_p)
            accessory_p = []
            exercises_to_exclude.extend(accessory_p)
            finisher_p = get_random_exercises(db_session, count=1, experienceLevel = programDifficulty, difficultyLevel = 5, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "any", availableEquipments = availableEquipments, exercisesToExclude=exercises_to_exclude)
            exercises_to_exclude.extend(finisher_p)

        case 75 | 90:
            warm_up_p = get_random_exercises(db_session, count=1, experienceLevel = programDifficulty, difficultyLevel = 3, targetedMuscleGroups = ["Cardiovascular system"], targetedMuscleType = "main", availableEquipments = availableEquipments, exercisesToExclude=exercises_to_exclude)
            exercises_to_exclude.extend(warm_up_p)
            activation_p = get_random_exercises(db_session, count=2, experienceLevel = programDifficulty, difficultyLevel = 5, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "secondary", availableEquipments = availableEquipments, exercisesToExclude=exercises_to_exclude)
            exercises_to_exclude.extend(activation_p)
            main_p = get_random_exercises(db_session, count=3, experienceLevel = programDifficulty, difficultyLevel = 7, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "main", availableEquipments = availableEquipments, exercisesToExclude=exercises_to_exclude)
            exercises_to_exclude.extend(main_p)
            accessory_p = get_random_exercises(db_session, count=1, experienceLevel = programDifficulty, difficultyLevel = 6, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "any", availableEquipments = availableEquipments, exercisesToExclude=exercises_to_exclude)
            exercises_to_exclude.extend(accessory_p)
            finisher_p = get_random_exercises(db_session, count=2, experienceLevel = programDifficulty, difficultyLevel = 4, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "any", availableEquipments = availableEquipments, exercisesToExclude=exercises_to_exclude)
            exercises_to_exclude.extend(finisher_p)
        case 105 | 120:
            warm_up_p = get_random_exercises(db_session, count=1, experienceLevel = programDifficulty, difficultyLevel = 3, targetedMuscleGroups = ["Cardiovascular system"], targetedMuscleType = "main", availableEquipments = availableEquipments, exercisesToExclude=exercises_to_exclude)
            exercises_to_exclude.extend(warm_up_p)
            activation_p = get_random_exercises(db_session, count=3, experienceLevel = programDifficulty, difficultyLevel = 5, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "secondary", availableEquipments = availableEquipments, exercisesToExclude=exercises_to_exclude)
            exercises_to_exclude.extend(activation_p)
            main_p = get_random_exercises(db_session, count=4, experienceLevel = programDifficulty, difficultyLevel = 7, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "main", availableEquipments = availableEquipments, exercisesToExclude=exercises_to_exclude)
            exercises_to_exclude.extend(main_p)
            accessory_p = get_random_exercises(db_session, count=2, experienceLevel = programDifficulty, difficultyLevel = 6, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "any", availableEquipments = availableEquipments, exercisesToExclude=exercises_to_exclude)
            exercises_to_exclude.extend(accessory_p)
            finisher_p = get_random_exercises(db_session, count=2, experienceLevel = programDifficulty, difficultyLevel = 4, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "any", availableEquipments = availableEquipments, exercisesToExclude=exercises_to_exclude)
            exercises_to_exclude.extend(finisher_p)

    workout = add_exercises_to_workout(workout, warm_up_p, "warm_up_p", programGoal)
    workout = add_exercises_to_workout(workout, activation_p, "activation_p", programGoal)
    workout = add_exercises_to_workout(workout, main_p, "main_p", programGoal)
    workout = add_exercises_to_workout(workout, accessory_p, "accessory_p", programGoal)
    workout = add_exercises_to_workout(workout, finisher_p, "finisher_p", programGoal)

    return workout

def add_exercises_to_workout(workout, exercises, programPart, programGoal):
    setsMult, repsMult, restMult = get_program_params(programPart, programGoal)
    for exercise in exercises:

        if exercise.repsType == "time":
            reps = max(1,round(exercise.defaultReps * repsMult) + randrange(-10, 10, 5))
        elif exercise.repsType == "reps":
            reps = max(1,round(exercise.defaultReps * repsMult) + randint(-1, 1))

        exo = {
            "Name": exercise.name,
            "Description": exercise.description,
            "Sets": max(1,round(exercise.defaultSets * setsMult)  + randint(-1, 1)),
            "Reps": reps,
            "Rest": max(1,round(exercise.defaultRest * restMult) + randrange(-10, 10, 5)),
            "RepsType": exercise.repsType
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
    "warm_up_p": {
        "strength": {"setsMult": 1, "repsMult": 1, "restMult": 1},
        "hypertrophy": {"setsMult": 1, "repsMult": 1, "restMult": 1},
        "endurance": {"setsMult": 1, "repsMult": 1, "restMult": 1},
    },
    "activation_p": {
        "strength": {"setsMult": 2, "repsMult": 1, "restMult": 1.5},
        "hypertrophy": {"setsMult": 1, "repsMult": 1.5, "restMult": 1},
        "endurance": {"setsMult": 1, "repsMult": 2, "restMult": 1},
    },
    "main_p": {
        "strength": {"setsMult": 2, "repsMult": 0.5, "restMult": 2.4},
        "hypertrophy": {"setsMult": 1.5, "repsMult": 1, "restMult": 1},
        "endurance": {"setsMult": 1, "repsMult": 2, "restMult": 1},
    },
    "accessory_p": {
        "strength": {"setsMult": 2, "repsMult": 1, "restMult": 1.5},
        "hypertrophy": {"setsMult": 1.5, "repsMult": 1, "restMult": 0.8},
        "endurance": {"setsMult": 1, "repsMult": 2, "restMult": 1},
    },
    "finisher_p": {
        "strength": {"setsMult": 1, "repsMult": 1, "restMult": 1},
        "hypertrophy": {"setsMult": 1, "repsMult": 1, "restMult": 1},
        "endurance": {"setsMult": 1, "repsMult": 1.2, "restMult": 1},
    },
}