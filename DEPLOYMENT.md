# Deployment Guide

## Production Deployment

### Option 1: Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: workflow_manager
      POSTGRES_PASSWORD: your_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  ollama:
    image: ollama/ollama:latest
    volumes:
      - ollama_data:/root/.ollama
    ports:
      - "11434:11434"

  backend:
    build: ./backend
    environment:
      DATABASE_URL: postgresql://postgres:your_password@postgres/workflow_manager
      OLLAMA_BASE_URL: http://ollama:11434
    depends_on:
      - postgres
      - ollama
    ports:
      - "8000:8000"

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

volumes:
  postgres_data:
  ollama_data:
```

### Option 2: Kubernetes

See `k8s/` directory for Kubernetes manifests.

### Option 3: Cloud Deployment

**AWS**
- ECS for containers
- RDS for PostgreSQL
- EC2 for Ollama (GPU instance)
- CloudFront for frontend

**GCP**
- Cloud Run for backend
- Cloud SQL for PostgreSQL
- Compute Engine for Ollama
- Cloud Storage for frontend

## Environment Variables

Production `.env`:

```env
# Database
DATABASE_URL=postgresql://user:pass@host:5432/dbname

# Ollama
OLLAMA_BASE_URL=http://ollama-host:11434
OLLAMA_MODEL=llama3.1

# Security
SECRET_KEY=generate-strong-random-key
ALLOWED_ORIGINS=https://yourdomain.com

# Integrations
JIRA_URL=https://your-domain.atlassian.net
JIRA_API_TOKEN=encrypted_token
STRIPE_API_KEY=encrypted_key
SMTP_PASSWORD=encrypted_password
```

## Performance Tuning

### Database
- Connection pooling: 20-50 connections
- Enable query caching
- Create indexes on frequently queried fields

### Backend
- Gunicorn workers: 2-4 per CPU core
- Worker timeout: 300s for long workflows
- Enable async workers

### Ollama
- Use GPU acceleration
- Adjust context window size
- Enable model caching

## Monitoring

### Metrics to Track
- Workflow execution time
- Success/failure rates
- Tool call latency
- Database query performance
- Memory usage

### Tools
- Prometheus for metrics
- Grafana for dashboards
- Sentry for error tracking
- ELK stack for logs

## Backup Strategy

### Database Backups
- Daily automated backups
- Point-in-time recovery enabled
- Backup retention: 30 days

### Workflow Definitions
- Version control in Git
- Export/import functionality
- Disaster recovery plan

## Security Checklist

- [ ] HTTPS enabled
- [ ] API authentication required
- [ ] Secrets encrypted at rest
- [ ] Rate limiting configured
- [ ] CORS properly configured
- [ ] SQL injection prevention
- [ ] Input validation on all endpoints
- [ ] Regular security updates
