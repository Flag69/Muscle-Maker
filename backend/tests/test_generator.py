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
    assert sets == 3
    assert reps == 15
    assert rest == 60

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

def test_generate_workout():
    db_session = SessionLocal()
    workout = generate_workout(db_session, programDuration=60, programDifficulty=3, programGoal="strength", targetedMuscleGroups=["Chest"], availableEquipments=["Dumbbell"])
    assert len(workout) > 0
    # print(workout)
    db_session.close()