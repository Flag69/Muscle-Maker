from app.database.db_functions import get_random_exercises, get_all_exercises
from app.database.db import SessionLocal

def test_get_random_exercises_default():
    db_session = SessionLocal()
    exos = get_random_exercises(db_session)
    assert len(exos) == 1

def test_get_random_exercises_count_5():
    db_session = SessionLocal()
    exos = get_random_exercises(db_session, count = 5)
    for exo in exos:
        print(exo)
    assert len(exos) == 5

def test_get_random_exercises_count_1000():
    db_session = SessionLocal()
    exos = get_random_exercises(db_session, count = 1000)
    # db should contain less that 1000 exercises for now
    assert len(exos) < 1000

def test_get_random_exercises_params():
    db_session = SessionLocal()
    exos = get_random_exercises(db_session, 6, 2, 4, ["Chest", "Arms"], "Secondary", None)
    for exo in exos:
        print(exo.name)
        assert exo.experienceLevel <= 2
        assert exo.difficultyLevel <= 4
        assert "Arms" in exo.secondaryMuscles or "Chest" in exo.secondaryMuscles
    assert len(exos) == 6

