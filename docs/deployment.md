# Deployment Guide

This guide covers deploying the Task Tracker application using Docker or Podman.

## Quick Start with Docker

The fastest way to get started is using Docker Compose:

```bash
# Clone the repository
git clone https://github.com/darrylbowler72/simplefullstack.git
cd simplefullstack

# Start all services
docker compose up --build

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Documentation: http://localhost:8000/docs
```

## Deployment Options

### 1. Docker Compose (Recommended for Development)

Perfect for local development and testing:

```bash
docker compose up --build
```

This will start:
- PostgreSQL database on port 5432
- FastAPI backend on port 8000
- Next.js frontend on port 3000

### 2. Podman (Docker Alternative)

For those preferring Podman, see the [Podman Deployment Guide](podman-deployment.md) for detailed instructions.

### 3. Production Deployment

For production deployments, consider:

- **Container Orchestration**: Kubernetes, Docker Swarm, or Nomad
- **Cloud Platforms**: AWS ECS, Google Cloud Run, Azure Container Instances
- **Platform as a Service**: Heroku, Railway, Render

## Environment Variables

### Backend
- `DATABASE_URL`: PostgreSQL connection string
  - Default: `postgresql://postgres:postgres@db:5432/tasktracker`

### Frontend
- `NEXT_PUBLIC_API_URL`: Backend API URL
  - Default: `http://localhost:8000`

## Stopping the Application

### Docker Compose
```bash
# Stop services
docker compose down

# Stop and remove volumes
docker compose down -v
```

### Podman
```bash
# Stop services
podman-compose down

# Stop and remove volumes
podman-compose down -v
```

## Health Checks

Verify the application is running:

```bash
# Check backend health
curl http://localhost:8000/docs

# Check frontend
curl http://localhost:3000

# Check database
docker compose exec db pg_isready -U postgres
```

## Troubleshooting

### Port Already in Use
If you see port conflict errors:
```bash
# Find process using port 3000
lsof -i :3000  # Linux/Mac
netstat -ano | findstr :3000  # Windows

# Kill the process or change ports in docker-compose.yml
```

### Database Connection Errors
```bash
# Check database logs
docker compose logs db

# Verify database is running
docker compose ps

# Restart database
docker compose restart db
```

### Frontend Can't Connect to Backend
- Ensure `NEXT_PUBLIC_API_URL` is set correctly
- Check if backend is running: `curl http://localhost:8000/docs`
- Verify network connectivity between containers

## CI/CD Integration

The repository includes GitHub Actions workflows for automated deployment. See `.github/workflows/` for examples of:
- Building and testing
- Deploying with Podman
- Running health checks

## Security Considerations

For production deployments:
1. Change default database credentials
2. Use environment-specific secrets
3. Enable HTTPS/TLS
4. Configure CORS appropriately
5. Implement rate limiting
6. Add authentication and authorization

## Monitoring

Consider adding:
- **Logging**: Centralized log aggregation (ELK, Loki)
- **Metrics**: Prometheus + Grafana
- **Tracing**: Jaeger or Zipkin
- **Health Checks**: Regular endpoint monitoring
