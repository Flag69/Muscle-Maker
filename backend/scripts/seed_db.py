import json

# Improvement: Do one big query instead of one query per exercise to check if it exists. This will reduce the number of queries to the database and improve performance.
# Run from appropriate folder for now, otherwise path problems

from app.database.db import SessionLocal
from app.database.models import Exercise

try:
    with open("data/exercises.json", "r", encoding="utf-8") as file:
        exercises = json.load(file)

    db = SessionLocal()

    added = 0
    for exercise in exercises:

        existing = (
            db.query(Exercise)
            .filter(Exercise.name == exercise["name"])
            .first()
        )

        if existing:
            print(f"Exercise '{exercise['name']}' already exists. Skipping.")
            continue

        db.add(Exercise(**exercise))
        added += 1

    db.commit()

except Exception:
    if db:
        db.rollback()
    raise
finally:
    if db:
        db.close()

print(f"Added {added} exercises.")