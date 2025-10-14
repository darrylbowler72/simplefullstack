# Task Tracker Application

This is a full-stack task management application that allows users to create, update, and delete tasks.

## Architecture

The system includes:
- **Frontend**: React with Next.js 15 and TypeScript
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL 15
- **Deployment**: Docker and Docker Compose

## Features

- ✅ Create new tasks with title and description
- ✅ Mark tasks as complete/incomplete
- ✅ Delete tasks
- ✅ Responsive UI with Tailwind CSS
- ✅ Dark mode support
- ✅ RESTful API
- ✅ Docker containerization

## Prerequisites

- Docker and Docker Compose installed on your system
- For local development without Docker:
  - Node.js 20+ and npm
  - Python 3.11+
  - PostgreSQL 15+

## Quick Start with Docker

1. Clone the repository:
```bash
git clone https://github.com/darrylbowler72/simplefullstack.git
cd simplefullstack
```

2. Start all services:
```bash
docker-compose up --build
```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Local Development (without Docker)

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Set up PostgreSQL database:
```bash
# Create a database named 'tasktracker'
# Update DATABASE_URL in app/database.py if needed
```

4. Run the backend:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

4. Open http://localhost:3000 in your browser

## API Endpoints

- `GET /tasks` - Get all tasks
- `GET /tasks/{id}` - Get a specific task
- `POST /tasks` - Create a new task
- `PUT /tasks/{id}` - Update a task
- `DELETE /tasks/{id}` - Delete a task

## Project Structure

```
simplefullstack/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI application
│   │   ├── models.py        # Database models
│   │   ├── schemas.py       # Pydantic schemas
│   │   └── database.py      # Database configuration
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── app/
│   │   ├── components/      # React components
│   │   ├── api.ts          # API client
│   │   ├── types.ts        # TypeScript types
│   │   ├── page.tsx        # Main page
│   │   └── layout.tsx      # Root layout
│   ├── Dockerfile
│   └── package.json
└── docker-compose.yml
```

## Environment Variables

### Backend
- `DATABASE_URL`: PostgreSQL connection string (default: `postgresql://postgres:postgres@db:5432/tasktracker`)

### Frontend
- `NEXT_PUBLIC_API_URL`: Backend API URL (default: `http://localhost:8000`)

## Stopping the Application

To stop all services:
```bash
docker-compose down
```

To stop and remove all data:
```bash
docker-compose down -v
```

## License

MIT
