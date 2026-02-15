from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base


class Idea(Base):
    """Idea model for storing user ideas."""
    
    __tablename__ = "ideas"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    def __repr__(self):
        return f"<Idea(id={self.id}, text='{self.text[:20]}...', created_at={self.created_at})>"
