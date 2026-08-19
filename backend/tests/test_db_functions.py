from app.database.db_functions import get_random_exercises, get_all_exercises
from app.database.db import SessionLocal

def test_get_random_exercises_default():
    db_session = SessionLocal()
    exos = get_random_exercises(db_session)
    assert len(exos) == 1
    db_session.close()

def test_get_random_exercises_count_5():
    db_session = SessionLocal()
    exos = get_random_exercises(db_session, count = 5)
    assert len(exos) == 5
    db_session.close()

def test_get_random_exercises_count_1000():
    db_session = SessionLocal()
    exos = get_random_exercises(db_session, count = 1000)
    # db should contain less that 1000 exercises for now
    assert len(exos) < 1000
    db_session.close()

def test_get_random_exercises_params_1():
    db_session = SessionLocal()
    exos = get_random_exercises(db_session, 3, 2, 4, ["Chest", "Arms"], "secondary", None)
    for exo in exos:
        assert exo.experienceLevel <= 2
        assert exo.difficultyLevel <= 4
        assert "Arms" in exo.secondaryMuscles or "Chest" in exo.secondaryMuscles
    assert len(exos) == 3
    db_session.close()

def test_get_random_exercises_params_2():
    db_session = SessionLocal()
    exos = get_random_exercises(db_session, 3, 2, 4, ["Everything"], "secondary", ["Everything"])
    for exo in exos:
        assert exo.experienceLevel <= 2
        assert exo.difficultyLevel <= 4
    assert len(exos) == 3
    db_session.close()

def test_get_random_exercises_params_3():
    db_session = SessionLocal()
    exos = get_random_exercises(db_session, 3, 2, 4, ["Cardiovascular system"], "main", ["Everything"])
    for exo in exos:
        assert exo.experienceLevel <= 2
        assert exo.difficultyLevel <= 4
        print(exo.name, exo.primaryMuscles)
        assert "Cardiovascular system" in exo.primaryMuscles
    assert len(exos) == 3
    db_session.close()

def test_get_random_exercises_params_4():
    db_session = SessionLocal()
    exos = get_random_exercises(db_session, 1, 4, 3, ["Cardiovascular system"], "main", ["Everything"])
    for exo in exos:
        assert exo.experienceLevel <= 4
        assert exo.difficultyLevel <= 3
        print(exo.name, exo.primaryMuscles)
        assert "Cardiovascular system" in exo.primaryMuscles
    assert len(exos) == 1
    db_session.close()

def test_get_random_exercises_params_5():
    db_session = SessionLocal()
    exos = get_random_exercises(db_session, 1, 3, 3, ["Cardiovascular system"], "main", ["Everything"])
    for exo in exos:
        assert exo.experienceLevel <= 3
        assert exo.difficultyLevel <= 3
        print(exo.name, exo.primaryMuscles)
        assert "Cardiovascular system" in exo.primaryMuscles
    assert len(exos) == 1
    db_session.close()

def test_get_random_exercises_params_exclusion_1():
    db_session = SessionLocal()
    exos_to_exclude = get_random_exercises(db_session, 3, 3, 3, ["Everything"], "main", ["Everything"])
    exos = get_random_exercises(db_session, 1, 3, 3, ["Everything"], "main", ["Everything"], exercisesToExclude=exos_to_exclude)
    for exo in exos:
        assert exo.experienceLevel <= 3
        assert exo.difficultyLevel <= 3
        print(exo.name, exo.primaryMuscles)
        assert exo not in exos_to_exclude
    assert len(exos) == 1
    db_session.close()

def test_get_random_exercises_params_exclusion_2():
    db_session = SessionLocal()
    exos_to_exclude = get_random_exercises(db_session, 3, 3, 3, ["Everything"], "main", ["Everything"])
    exos = get_random_exercises(db_session, 1, 3, 3, ["Everything"], "main", ["Everything"], exercisesToExclude=exos_to_exclude)
    for exo in exos:
        assert exo.experienceLevel <= 3
        assert exo.difficultyLevel <= 3
        print(exo.name, exo.primaryMuscles)
        assert exo not in exos_to_exclude
    assert len(exos) == 1
    db_session.close()

def test_get_all_exercises():
    db_session = SessionLocal()
    exos = get_all_exercises(db_session)
    # db contains 45 exos as I am writing this test
    assert len(exos) >= 45
    db_session.close()
