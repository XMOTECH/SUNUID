from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.db import SessionLocal, init_db

app = FastAPI(title="SUNUID Backend")

@app.on_event("startup")
def on_startup():
    init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    return {"status": "ok"}
