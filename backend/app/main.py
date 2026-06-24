# Implements FastAPI, CORS, basic endpoints and includes other endpoints files

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend is running!"}