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