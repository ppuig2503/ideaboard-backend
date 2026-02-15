from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import Idea
from ..schemas import IdeaCreate, IdeaResponse

router = APIRouter(
    prefix="/ideas",
    tags=["ideas"]
)


@router.get("", response_model=List[IdeaResponse])
def get_ideas(db: Session = Depends(get_db)):
    """
    Retrieve all ideas.
    
    Returns a list of all ideas ordered by creation date (newest first).
    """
    ideas = db.query(Idea).order_by(Idea.created_at.desc()).all()
    return ideas


@router.post("", response_model=IdeaResponse, status_code=status.HTTP_201_CREATED)
def create_idea(idea: IdeaCreate, db: Session = Depends(get_db)):
    """
    Create a new idea.
    
    Args:
        idea: The idea data to create
        db: Database session dependency
    
    Returns:
        The created idea with id and timestamp
    """
    # Create new idea instance
    db_idea = Idea(text=idea.text)
    
    # Add to database
    db.add(db_idea)
    db.commit()
    db.refresh(db_idea)
    
    return db_idea
