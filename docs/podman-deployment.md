# Podman Deployment Guide

This guide explains how to deploy the Task Tracker application using Podman, a daemonless container engine that serves as a Docker alternative.

## What is Podman?

Podman is a container engine that provides a Docker-compatible command-line interface without requiring a daemon process. It's more secure and can run rootless containers.

## Prerequisites

1. **Install Podman**
   - **Ubuntu/Debian**: `sudo apt-get install podman`
   - **Fedora/RHEL**: `sudo dnf install podman`
   - **macOS**: `brew install podman`
   - **Windows**: Download from [podman.io](https://podman.io)

2. **Install podman-compose** (optional, for compose file support)
   ```bash
   pip install podman-compose
   ```

## Deployment Methods

### Method 1: Using podman-compose (Recommended)

This is the easiest method, similar to Docker Compose:

```bash
# Clone the repository
git clone https://github.com/darrylbowler72/simplefullstack.git
cd simplefullstack

# Start all services
podman-compose up --build

# Stop services
podman-compose down
```

### Method 2: Using Podman CLI

For more control, you can use Podman commands directly:

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

### Method 3: GitHub Actions CI/CD

The repository includes a GitHub Actions workflow that automatically deploys using Podman:

- **Workflow file**: `.github/workflows/deploy-podman.yml`
- **Trigger**: Automatically on push to `main` branch
- **Manual trigger**: Via workflow_dispatch in GitHub Actions UI

The workflow:
1. Installs Podman and podman-compose
2. Builds all container images
3. Creates network and deploys containers
4. Verifies the deployment
5. Runs health checks
6. Displays logs for debugging

## Accessing the Application

Once deployed, access the application at:

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Managing Containers

### View running containers
```bash
podman ps
```

### View logs
```bash
podman logs tasktracker-frontend
podman logs tasktracker-backend
podman logs tasktracker-db
```

### Stop containers
```bash
podman stop tasktracker-frontend tasktracker-backend tasktracker-db
```

### Remove containers
```bash
podman rm tasktracker-frontend tasktracker-backend tasktracker-db
```

### Remove network
```bash
podman network rm tasktracker-network
```

### Clean up everything
```bash
podman stop tasktracker-frontend tasktracker-backend tasktracker-db
podman rm tasktracker-frontend tasktracker-backend tasktracker-db
podman network rm tasktracker-network
podman volume prune -f
```

## Troubleshooting

### Container won't start
```bash
# Check container logs
podman logs <container-name>

# Check container status
podman ps -a
```

### Database connection issues
```bash
# Verify database is running
podman exec tasktracker-db pg_isready -U postgres

# Check database logs
podman logs tasktracker-db
```

### Network issues
```bash
# List networks
podman network ls

# Inspect network
podman network inspect tasktracker-network
```

### Port conflicts
If ports 3000, 8000, or 5432 are already in use:
```bash
# Find process using port
sudo lsof -i :3000
sudo lsof -i :8000
sudo lsof -i :5432

# Modify ports in podman-compose.yml or use different ports in CLI
```

## Differences from Docker

Podman is designed to be Docker-compatible, but there are some differences:

1. **No daemon**: Podman runs without a background daemon
2. **Rootless**: Can run containers without root privileges
3. **Security**: Better isolation and security features
4. **Systemd integration**: Native support for systemd unit files
5. **Pod support**: Can group containers into pods (Kubernetes-compatible)

## Converting from Docker

If you're familiar with Docker:

- `docker` → `podman` (commands are mostly identical)
- `docker-compose` → `podman-compose`
- Docker networks → Podman networks (compatible)
- Docker volumes → Podman volumes (compatible)

Most Docker commands work with Podman by simply replacing `docker` with `podman`.

## Additional Resources

- [Podman Documentation](https://docs.podman.io)
- [podman-compose GitHub](https://github.com/containers/podman-compose)
- [Migrating from Docker to Podman](https://podman.io/getting-started/migration)
