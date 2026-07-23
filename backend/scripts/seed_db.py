import json

from app.db import SessionLocal
from app.models import Exercise

db = SessionLocal()

with open("../data/exercises.json", "r") as file:
    exercises = json.load(file)

for exercise in exercises:
    db.add(Exercise(**exercise))

db.commit()
db.close()

print(f"Added {len(exercises)} exercises.")