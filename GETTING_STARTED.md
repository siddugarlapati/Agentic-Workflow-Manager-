# 🚀 Getting Started Guide

Welcome! This guide will help you get the Autonomous Agentic Workflow Manager up and running in minutes.

## 📋 Prerequisites

Before you begin, ensure you have:

- **Docker** and **Docker Compose** installed
- **8GB RAM** minimum (16GB recommended)
- **10GB disk space** for Docker images and models
- **macOS, Linux, or Windows** with WSL2

## ⚡ Quick Start (5 Minutes)

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd workflow-manager
```

### Step 2: Run Quick Start Script

```bash
./quickstart.sh
```

This script will:
- ✅ Check Docker installation
- ✅ Start all services (PostgreSQL, Ollama, Backend, Frontend)
- ✅ Pull the Llama 3.1 model
- ✅ Initialize the database

### Step 3: Access the Application

Open your browser and navigate to:

- **Frontend**: http://localhost:5173
- **API Documentation**: http://localhost:8000/docs
- **Backend API**: http://localhost:8000

## 🎯 First Workflow

Let's create and execute your first workflow!

### 1. Create a Simple Workflow

Open a new terminal and run:

```bash
curl -X POST http://localhost:8000/api/workflows \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Workflow",
    "description": "My first workflow",
    "definition": {
      "steps": [
        {
          "id": 1,
          "name": "Send Email",
          "tool": "send_email",
          "parameters": {
            "to_email": "test@example.com",
            "subject": "Test Email",
            "body": "Hello from the workflow manager!"
          }
        }
      ]
    }
  }'
```

### 2. Execute the Workflow

```bash
curl -X POST http://localhost:8000/api/executions \
  -H "Content-Type: application/json" \
  -d '{
    "workflow_id": 1,
    "input_data": {}
  }'
```

### 3. Check Execution Status

```bash
curl http://localhost:8000/api/executions/1
```

You should see the execution status and trace!

## 🎨 Using the Frontend

### Dashboard
1. Navigate to http://localhost:5173
2. View execution statistics
3. See recent activity

### Create a Workflow
1. Click "Workflows" in the navigation
2. Click "New Workflow" button
3. Fill in the details:
   - Name: "Client Onboarding"
   - Description: "Automated client onboarding process"
   - Steps: Define your workflow steps

### Execute a Workflow
1. Go to "Workflows" page
2. Find your workflow
3. Click "Execute" button
4. Provide input parameters
5. Monitor execution in real-time

### View Results
1. Go to "Executions" page
2. Click on an execution
3. View the execution trace
4. See agent decisions and tool calls

## 🔧 Configuration

### Environment Variables

Edit `backend/.env`:

```env
# Database
DATABASE_URL=postgresql://localhost/workflow_manager

# Ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.1

# Jira (optional)
JIRA_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your_token

# Stripe (optional)
STRIPE_API_KEY=sk_test_your_key

# Email (optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@example.com
SMTP_PASSWORD=your_app_password
```

### Tool Configuration

To use Jira, Stripe, or Email tools:

1. Get API credentials from the respective services
2. Add them to `backend/.env`
3. Restart the backend: `docker-compose restart backend`

## 📚 Example Workflows

### Client Onboarding

```bash
curl -X POST http://localhost:8000/api/workflows \
  -H "Content-Type: application/json" \
  -d @backend/app/templates/client_onboarding.json
```

Then execute:

```bash
curl -X POST http://localhost:8000/api/executions \
  -H "Content-Type: application/json" \
  -d '{
    "workflow_id": 1,
    "input_data": {
      "client_name": "Acme Corp",
      "client_email": "contact@acme.com",
      "client_code": "ACME",
      "project_lead_id": "user123",
      "subscription_plan_id": "price_1234"
    }
  }'
```

## 🐛 Troubleshooting

### Services Not Starting

```bash
# Check Docker status
docker ps

# View logs
docker-compose logs backend
docker-compose logs frontend
docker-compose logs ollama
```

### Database Connection Issues

```bash
# Restart PostgreSQL
docker-compose restart postgres

# Check database
docker exec -it workflow-manager-postgres-1 psql -U postgres -d workflow_manager
```

### Ollama Model Not Loading

```bash
# Pull model manually
docker exec -it workflow-manager-ollama-1 ollama pull llama3.1

# Check available models
docker exec -it workflow-manager-ollama-1 ollama list
```

### Frontend Not Loading

```bash
# Rebuild frontend
cd frontend
npm install
npm run build

# Or restart container
docker-compose restart frontend
```

## 🔄 Stopping and Restarting

### Stop All Services

```bash
docker-compose down
```

### Stop and Remove Data

```bash
docker-compose down -v
```

### Restart Services

```bash
docker-compose up -d
```

### View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
```

## 📖 Next Steps

Now that you're up and running:

1. **Read the Documentation**
   - [ARCHITECTURE.md](./ARCHITECTURE.md) - Understand the system
   - [EXAMPLES.md](./EXAMPLES.md) - More usage examples
   - [FEATURES.md](./FEATURES.md) - Feature breakdown

2. **Explore the API**
   - Visit http://localhost:8000/docs
   - Try different endpoints
   - Test with Postman or curl

3. **Create Custom Workflows**
   - Define your own workflows
   - Add custom tools
   - Integrate with your systems

4. **Deploy to Production**
   - Read [DEPLOYMENT.md](./DEPLOYMENT.md)
   - Configure for production
   - Set up monitoring

## 💡 Tips

### Performance
- Use SSD for Docker volumes
- Allocate at least 4GB RAM to Docker
- Use GPU for Ollama if available

### Development
- Enable hot reload for faster development
- Use the API docs for testing
- Check logs frequently

### Production
- Use environment variables for secrets
- Enable HTTPS
- Set up monitoring and alerts
- Regular backups

## 🆘 Getting Help

If you run into issues:

1. **Check the logs**: `docker-compose logs`
2. **Read the docs**: All .md files in the root
3. **Search issues**: GitHub issue tracker
4. **Ask for help**: GitHub discussions

## 🎉 Success!

You now have a fully functional autonomous workflow automation system!

Try creating your first workflow and watch the AI agents work together to execute it.

---

**Autonomous Workflow Automation - Production Ready**
