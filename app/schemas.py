from datetime import datetime
from pydantic import BaseModel, Field


class IdeaBase(BaseModel):
    """Base schema for Idea with common attributes."""
    text: str = Field(..., min_length=1, max_length=1000, description="The idea text")


class IdeaCreate(IdeaBase):
    """Schema for creating a new idea."""
    pass


class IdeaResponse(IdeaBase):
    """Schema for idea response."""
    id: int
    created_at: datetime
    
    class Config:
        """Pydantic config."""
        from_attributes = True  # Allows compatibility with ORM models


class HealthResponse(BaseModel):
    """Schema for health check response."""
    status: str
    environment: str
    timestamp: datetime
