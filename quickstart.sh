#!/bin/bash

echo "🚀 Autonomous Agentic Workflow Manager - Quick Start"
echo "=================================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"
echo ""

# Start services
echo "📦 Starting services with Docker Compose..."
docker-compose up -d

echo ""
echo "⏳ Waiting for services to be ready..."
sleep 15

# Get the actual container name for backend
BACKEND_CONTAINER=$(docker-compose ps -q backend)

# Pull Ollama model
echo ""
echo "🤖 Pulling Llama 3.1 model (this may take a few minutes)..."
docker exec $BACKEND_CONTAINER sh -c "curl -X POST http://ollama:11434/api/pull -d '{\"name\":\"llama3.1\"}'" 2>/dev/null || echo "Note: Model will be pulled on first use"

echo ""
echo "✅ Setup complete!"
echo ""
echo "📍 Access the application:"
echo "   Frontend: http://localhost:5173"
echo "   Backend API: http://localhost:8000"
echo "   API Docs: http://localhost:8000/docs"
echo ""
echo "📚 Next steps:"
echo "   1. Open http://localhost:5173 in your browser"
echo "   2. Check out EXAMPLES.md for usage examples"
echo "   3. Read SETUP.md for manual setup instructions"
echo ""
echo "🛑 To stop services: docker-compose down"
echo ""
