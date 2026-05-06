# Setup Guide

## 1. Install Ollama (Local LLM)

```bash
# macOS
brew install ollama

# Start Ollama service
ollama serve

# Pull a model (in another terminal)
ollama pull llama3.1
```

## 2. Setup PostgreSQL

```bash
# macOS
brew install postgresql@15
brew services start postgresql@15

# Create database
createdb workflow_manager
```

## 3. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your configuration

# Run migrations
alembic upgrade head

# Start backend server
uvicorn app.main:app --reload --port 8000
```

## 4. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

## 5. Access the Application

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```env
DATABASE_URL=postgresql://localhost/workflow_manager
OLLAMA_BASE_URL=http://localhost:11434
JIRA_API_KEY=your_jira_key
STRIPE_API_KEY=your_stripe_key
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email
SMTP_PASSWORD=your_password
```

## Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```
