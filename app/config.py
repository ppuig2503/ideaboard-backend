import os
from dotenv import load_dotenv

# Load environment variables from .env file in development
load_dotenv()


class Settings:
    """Application settings and configuration."""
    
    # Environment
    ENV: str = os.getenv("ENV", "production")
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    
    # Server
    PORT: int = int(os.getenv("PORT", "8000"))
    
    # CORS
    @property
    def CORS_ORIGINS(self) -> list:
        """Configure CORS origins based on environment."""
        if self.ENV == "development":
            return [
                "http://localhost:3000",
                "http://localhost:5173",
                "http://localhost:8000",
            ]
        else:
            # Add your production frontend URL here
            return [
                "https://your-frontend-domain.com",
            ]
    
    @property
    def is_production(self) -> bool:
        """Check if running in production."""
        return self.ENV == "production"


settings = Settings()
