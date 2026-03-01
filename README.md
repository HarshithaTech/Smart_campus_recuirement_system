# SmartHire Agentic Platform (2026)

## Setup Instructions

### Backend
1. `cd backend`
2. `pip install -r requirements.txt`
3. Create a `.env` file based on `.env.example` and add your `GEMINI_API_KEY`.
4. Run locally: `uvicorn app.main:app --reload`

### Frontend
1. `cd frontend`
2. `npm install`
3. Run locally: `npm run dev`

### Database
1. Requires PostgreSQL with `pgvector` extension.
2. Apply schema: `psql -d smarthire -f ../db/schema.sql`

## Docker Deployment
```bash
docker-compose up --build
```
