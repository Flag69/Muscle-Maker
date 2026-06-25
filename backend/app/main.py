# Implements FastAPI, CORS, basic endpoints, includes other endpoints files, creates database tables, and runs the application.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.exercises_endpoints import router as exercises_router
from app.database.db import create_tables

create_tables()  # Create database and its tables if they don't exist

app = FastAPI()
app.include_router(exercises_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend is running!"}

