from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

from .config import settings
from .database import init_db
from .schemas import HealthResponse
from .routes import ideas

# Create FastAPI application
app = FastAPI(
    title="Ideaboard Backend",
    description="A production-ready FastAPI backend for managing ideas",
    version="1.0.0",
    docs_url="/docs" if not settings.is_production else None,  # Disable docs in production
    redoc_url="/redoc" if not settings.is_production else None,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(ideas.router)


@app.on_event("startup")
async def startup_event():
    """
    Run on application startup.
    Initializes the database tables.
    """
    print(f"Starting application in {settings.ENV} environment...")
    print(f"Database URL: {settings.DATABASE_URL.split('@')[-1]}")  # Log without credentials
    init_db()
    print("Database initialized successfully!")


@app.get("/health", response_model=HealthResponse, tags=["health"])
async def health_check():
    """
    Health check endpoint.
    
    Returns the current status of the application.
    """
    return HealthResponse(
        status="healthy",
        environment=settings.ENV,
        timestamp=datetime.now()
    )


@app.get("/", tags=["root"])
async def root():
    """
    Root endpoint.
    
    Returns a welcome message.
    """
    return {
        "message": "Welcome to Ideaboard Backend API",
        "version": "1.0.0",
        "docs": "/docs" if not settings.is_production else "disabled",
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.PORT,
        reload=not settings.is_production,
    )
