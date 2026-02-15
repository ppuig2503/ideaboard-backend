# Ideaboard Backend

A production-ready FastAPI backend for managing ideas with PostgreSQL database.

## Features

- ✅ FastAPI framework with automatic API documentation
- ✅ PostgreSQL database with SQLAlchemy ORM
- ✅ Environment-based configuration (dev/prod)
- ✅ CORS middleware properly configured
- ✅ Pydantic schemas for request/response validation
- ✅ Database session dependency injection
- ✅ Health check endpoint
- ✅ Ready for deployment on Render

## Project Structure

```
ideaboard-backend/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application
│   ├── config.py         # Configuration management
│   ├── database.py       # Database setup
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   └── routes/
│       ├── __init__.py
│       └── ideas.py      # Ideas endpoints
├── .env                  # Environment variables (local)
├── .gitignore
├── requirements.txt
└── README.md
```

## API Endpoints

### Health Check
- `GET /health` - Health check endpoint

### Ideas
- `GET /ideas` - Get all ideas (ordered by newest first)
- `POST /ideas` - Create a new idea

### Documentation
- `GET /docs` - Swagger UI (disabled in production)
- `GET /redoc` - ReDoc documentation (disabled in production)

## Local Development Setup

### Prerequisites

- Python 3.9 or higher
- PostgreSQL database

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd ideaboard-backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
   - Copy `.env` and update with your database credentials:
```env
DATABASE_URL=postgresql://username:password@localhost:5432/ideaboard_dev
ENV=development
PORT=8000
```

5. Run the application:
```bash
python -m app.main
# or
uvicorn app.main:app --reload --port 8000
```

6. Access the API:
   - API: http://localhost:8000
   - Swagger Docs: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

## Deployment on Render

### Database Setup

1. Create a PostgreSQL database on Render
2. Copy the Internal Database URL

### Web Service Setup

1. Create a new Web Service on Render
2. Connect your repository
3. Configure the service:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

4. Add environment variables:
   - `DATABASE_URL`: (Use the Internal Database URL from Render)
   - `ENV`: `production`
   - `PORT`: (Automatically set by Render)

5. Deploy!

## Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `DATABASE_URL` | PostgreSQL connection string | - | ✅ |
| `ENV` | Environment (development/production) | production | ❌ |
| `PORT` | Server port | 8000 | ❌ |

## Database Schema

### Ideas Table

| Column | Type | Description |
|--------|------|-------------|
| `id` | Integer | Primary key (auto-increment) |
| `text` | String | Idea text content |
| `created_at` | DateTime | Timestamp (auto-generated) |

## Testing

Example requests using curl:

### Get all ideas
```bash
curl http://localhost:8000/ideas
```

### Create a new idea
```bash
curl -X POST http://localhost:8000/ideas \
  -H "Content-Type: application/json" \
  -d '{"text": "Build an amazing product"}'
```

### Health check
```bash
curl http://localhost:8000/health
```

## Technologies

- **FastAPI** - Modern, fast web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **PostgreSQL** - Relational database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server
- **python-dotenv** - Environment variable management

## License

MIT License
