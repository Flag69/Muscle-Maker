from app.services.generator import get_program_params, add_exercises_to_workout, generate_workout
from app.database.db_functions import get_random_exercises, get_all_exercises
from app.database.db import SessionLocal


def test_get_program_params_1():
    sets, reps, rest = get_program_params("activation_p", "strength")
    assert sets == 2
    assert reps == 1
    assert rest == 1.5

def test_get_program_params_2():
    sets, reps, rest = get_program_params("main_p", "endurance")
    assert sets == 1
    assert reps == 2
    assert rest == 1

def test_add_exercises_to_workout_1():
    db_session = SessionLocal()
    workout = []
    exercises = get_random_exercises(db_session, count=3)
    add_exercises_to_workout(workout, exercises, "activation_p", "strength")
    assert len(workout) == 3
    # print(workout)
    db_session.close()

def test_add_exercises_to_workout_2():
    db_session = SessionLocal()
    workout = []
    exercises = get_random_exercises(db_session, count=8)
    add_exercises_to_workout(workout, exercises, "main_p", "hypertrophy")
    assert len(workout) == 8
    # print(workout)
    db_session.close()

def test_add_exercises_to_workout_3():
    db_session = SessionLocal()
    programDifficulty = 3
    programGoal = "strength"
    targetedMuscleGroups = ["Everything"]
    availableEquipments = ["Everything"]
    workout = []

    warm_up_p = get_random_exercises(db_session, count=1, experienceLevel = programDifficulty, difficultyLevel = 3, targetedMuscleGroups = ["Cardiovascular system"], targetedMuscleType = "main", availableEquipments = availableEquipments)
    assert len(warm_up_p) == 1
    activation_p = get_random_exercises(db_session, count=3, experienceLevel = programDifficulty, difficultyLevel = 5, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "secondary", availableEquipments = availableEquipments)
    assert len(activation_p) == 3
    main_p = get_random_exercises(db_session, count=4, experienceLevel = programDifficulty, difficultyLevel = 7, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "main", availableEquipments = availableEquipments)
    assert len(main_p) == 4
    accessory_p = get_random_exercises(db_session, count=2, experienceLevel = programDifficulty, difficultyLevel = 6, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "any", availableEquipments = availableEquipments)
    assert len(accessory_p) == 2
    finisher_p = get_random_exercises(db_session, count=2, experienceLevel = programDifficulty, difficultyLevel = 4, targetedMuscleGroups = targetedMuscleGroups, targetedMuscleType = "any", availableEquipments = availableEquipments)
    assert len(finisher_p) == 2

    workout = add_exercises_to_workout(workout, warm_up_p, "warm_up_p", programGoal)
    workout = add_exercises_to_workout(workout, activation_p, "activation_p", programGoal)
    workout = add_exercises_to_workout(workout, main_p, "main_p", programGoal)
    workout = add_exercises_to_workout(workout, accessory_p, "accessory_p", programGoal)
    workout = add_exercises_to_workout(workout, finisher_p, "finisher_p", programGoal)
    # print(workout)
    assert len(workout) == 12
    db_session.close()

def test_generate_workout_params_1():
    db_session = SessionLocal()
    workout = generate_workout(db_session, programDuration=60, programDifficulty=3, programGoal="strength", targetedMuscleGroups=["Chest"], availableEquipments=["Dumbbell"])
    assert len(workout) > 0
    # print(workout)
    db_session.close()

def test_generate_workout_params_2():
    db_session = SessionLocal()
    workout = generate_workout(db_session, programDuration=45, programDifficulty=2, programGoal="hypertrophy", targetedMuscleGroups=["Everything"], availableEquipments=["Barbell"])
    assert len(workout) > 0
    # print(workout)
    db_session.close()