# Contains functions to query the database

from app.database.models import Exercise

def create_exercise(db_session, name):
    new_exercise = Exercise(name=name)
    db_session.add(new_exercise)
    db_session.commit()
    db_session.refresh(new_exercise)
    return new_exercise

def get_all_exercises(db_session):
    return db_session.query(Exercise).all()

def get_random_exercises_main(db_session, count=1, experienceLevel = 4, difficultyLevel = 10, targetedMuscleGroups = ["Everything"], availableEquipments = ["Everything"]):
    query = db_session.query(Exercise)

    if experienceLevel:
        query = query.filter(Exercise.experienceLevel <= experienceLevel)
    if difficultyLevel:
        query = query.filter(Exercise.difficultyLevel <= difficultyLevel)
    if targetedMuscleGroups and "Everything" not in targetedMuscleGroups:
        query = query.filter(Exercise.primaryMuscles is in targetedMuscleGroups)
    if availableEquipments and "Everything" not in availableEquipments:
        query = query.filter(Exercise.requiredEquipments.contains(availableEquipments))

    return query.order_by(func.random()).limit(count).all()
    