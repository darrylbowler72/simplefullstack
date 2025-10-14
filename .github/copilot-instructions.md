# Copilot Instructions for Task Tracker Full-Stack App

## Architecture Overview

This is a **dockerized full-stack task management app** with clear separation between frontend, backend, and database:

- **Frontend**: Next.js 15 (`frontend/`) - React with TypeScript, Tailwind CSS, client-side rendering
- **Backend**: FastAPI (`backend/app/`) - Python API with SQLAlchemy ORM
- **Database**: PostgreSQL 15 via Docker Compose

The app follows **API-first architecture** - frontend communicates with backend exclusively through REST endpoints at `http://localhost:8000`.

## Key Development Patterns

### Docker-First Development
- **Primary workflow**: `docker compose up --build` starts all services
- **Database connection**: Backend uses `DATABASE_URL=postgresql://postgres:postgres@db:5432/tasktracker`
- **CORS configuration**: Backend allows `http://localhost:3000` for frontend access
- **Environment variables**: `NEXT_PUBLIC_API_URL=http://localhost:8000` for frontend API calls

### Backend Architecture (`backend/app/`)
- **Models**: SQLAlchemy models in `models.py` (e.g., `Task` with timestamps)
- **Schemas**: Pydantic models in `schemas.py` for request/response validation
- **Database**: Session management via dependency injection `Depends(get_db)`
- **API structure**: Standard CRUD endpoints with proper HTTP status codes
- **Testing**: Use `test_api.py` with SQLite for isolated testing

### Frontend Patterns (`frontend/app/`)
- **API layer**: Centralized in `api.ts` with error handling
- **State management**: React hooks (`useState`, `useEffect`) for local state
- **Component structure**: Reusable components in `components/` (TaskForm, TaskList, TaskItem)
- **Styling**: Tailwind CSS with dark mode support (`dark:` prefixes)
- **TypeScript**: Strict typing with interfaces in `types.ts`

## Critical Developer Commands

```bash
# Start entire stack
docker compose up --build

# Backend testing (standalone)
cd backend && python test_api.py

# Frontend development (if not using Docker)
cd frontend && npm run dev --turbopack

# Database access
docker exec -it tasktracker-db psql -U postgres -d tasktracker
```

## Database Schema Patterns

Tasks follow this SQLAlchemy pattern:
- Auto-generated `id` (primary key)
- Automatic timestamps: `created_at`, `updated_at` using `func.now()`
- Boolean flags with defaults: `completed = False`
- Nullable descriptions, required titles

## Frontend-Backend Integration

- **API base URL**: Always use `NEXT_PUBLIC_API_URL` environment variable
- **Error handling**: Frontend displays user-friendly messages for API failures
- **State updates**: Call refresh functions (e.g., `fetchTasks()`) after mutations
- **Loading states**: Show loading indicators during API calls
- **CORS**: Backend explicitly allows frontend origin in `main.py`

## Project-Specific Conventions

- **File organization**: Keep API logic in `api.ts`, not mixed with components
- **Component props**: Use callback functions for parent-child communication (e.g., `onTaskCreated`)
- **Database sessions**: Always use dependency injection, never create sessions directly
- **Environment handling**: Backend defaults to Docker hostnames (`db:5432`), frontend to localhost
- **Testing approach**: Use separate SQLite database for backend tests to avoid conflicts