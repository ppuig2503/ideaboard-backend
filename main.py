from fastapi import FastAPI
from database import SessionLocal, engine
from models import Base, Idea
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/ideas")
def get_ideas():
    db: Session = SessionLocal()
    ideas = db.query(Idea).all()
    return ideas

@app.post("/ideas")
def create_idea(idea: dict):
    db: Session = SessionLocal()
    new_idea = Idea(text=idea["text"])
    db.add(new_idea)
    db.commit()
    db.refresh(new_idea)
    return new_idea
