# Task Tracker Application

This is a full-stack task management application that allows users to create, update, and delete tasks.

## Architecture

The system includes:
- **Frontend**: React with Next.js 15 and TypeScript
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL 15
- **Deployment**: Docker/Podman and Docker Compose/Podman Compose

## Features

- ✅ Create new tasks with title and description
- ✅ Mark tasks as complete/incomplete
- ✅ Delete tasks
- ✅ Responsive UI with Tailwind CSS
- ✅ Dark mode support
- ✅ RESTful API
- ✅ Docker/Podman containerization
- ✅ GitHub Actions CI/CD with Podman deployment

## Prerequisites

- Docker and Docker Compose OR Podman and podman-compose installed on your system
- For local development without containers:
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
docker compose up --build
```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## Deployment with Podman

Podman is a daemonless container engine that can be used as a Docker alternative.

### Prerequisites
- Podman installed on your system
- podman-compose installed (`pip install podman-compose`)

### Deploy with Podman Compose

1. Clone the repository:
```bash
git clone https://github.com/darrylbowler72/simplefullstack.git
cd simplefullstack
```

2. Start all services:
```bash
podman-compose up --build
```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Deploy with Podman CLI

Alternatively, you can deploy using Podman commands directly:

```bash
# Create a network
podman network create tasktracker-network

# Run PostgreSQL
podman run -d \
  --name tasktracker-db \
  --network tasktracker-network \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=tasktracker \
  -p 5432:5432 \
  postgres:15-alpine

# Build and run backend
podman build -t tasktracker-backend:latest ./backend
podman run -d \
  --name tasktracker-backend \
  --network tasktracker-network \
  -e DATABASE_URL=postgresql://postgres:postgres@tasktracker-db:5432/tasktracker \
  -p 8000:8000 \
  tasktracker-backend:latest

# Build and run frontend
podman build -t tasktracker-frontend:latest ./frontend
podman run -d \
  --name tasktracker-frontend \
  --network tasktracker-network \
  -e NEXT_PUBLIC_API_URL=http://localhost:8000 \
  -p 3000:3000 \
  tasktracker-frontend:latest
```

### CI/CD with GitHub Actions

The repository includes a GitHub Actions workflow that automatically builds and deploys the application using Podman. The workflow is triggered on every push to the main branch and can also be manually triggered.

To view the workflow: `.github/workflows/deploy-podman.yml`

#### GitHub Self-Hosted Runner Setup

The CI/CD workflow uses a self-hosted GitHub Actions runner to build and deploy the application locally. Here's how to manage it:

**Starting the Runner**

The runner is typically installed at `C:\Users\[username]\actions-runner` (or `~/actions-runner` on Linux/Mac).

To start the runner manually:
```bash
cd C:\Users\[username]\actions-runner  # Windows
# or
cd ~/actions-runner  # Linux/Mac

# Start the runner
./run.cmd  # Windows
# or
./run.sh  # Linux/Mac
```

**Installing as a Windows Service (Recommended)**

For automatic startup, install the runner as a Windows service from an Administrator PowerShell:
```powershell
cd C:\Users\[username]\actions-runner
.\svc.cmd install
.\svc.cmd start
```

**Managing the Service**
```powershell
# Check status
.\svc.cmd status

# Stop the service
.\svc.cmd stop

# Uninstall the service
.\svc.cmd uninstall
```

**Verifying the Runner**

Check if the runner is active:
1. Go to your GitHub repository
2. Navigate to **Settings → Actions → Runners**
3. Verify your self-hosted runner shows as "Idle" (green) instead of "Offline" (gray)

**Note**: The runner must be running for the automated deployment workflow to execute. If the runner is offline, workflows will queue until it comes online.

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
├── .github/
│   └── workflows/
│       ├── build-and-test.yml    # CI workflow
│       └── deploy-podman.yml     # Podman deployment workflow
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI application
│   │   ├── models.py             # Database models
│   │   ├── schemas.py            # Pydantic schemas
│   │   └── database.py           # Database configuration
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── app/
│   │   ├── components/           # React components
│   │   ├── api.ts               # API client
│   │   ├── types.ts             # TypeScript types
│   │   ├── page.tsx             # Main page
│   │   └── layout.tsx           # Root layout
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml
└── podman-compose.yml
```

## Environment Variables

### Backend
- `DATABASE_URL`: PostgreSQL connection string (default: `postgresql://postgres:postgres@db:5432/tasktracker`)

### Frontend
- `NEXT_PUBLIC_API_URL`: Backend API URL (default: `http://localhost:8000`)

## Stopping the Application

### With Docker Compose
To stop all services:
```bash
docker compose down
```

To stop and remove all data:
```bash
docker compose down -v
```

### With Podman Compose
To stop all services:
```bash
podman-compose down
```

To stop and remove all data:
```bash
podman-compose down -v
```

### With Podman CLI
```bash
podman stop tasktracker-frontend tasktracker-backend tasktracker-db
podman rm tasktracker-frontend tasktracker-backend tasktracker-db
podman network rm tasktracker-network
```

## License

MIT
