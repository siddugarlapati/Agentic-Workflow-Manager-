from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.api import workflows, agents, tools, executions
from app.core.config import settings
from app.db.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize services on startup"""
    await init_db()
    yield


app = FastAPI(
    title="Agentic Workflow Manager",
    description="Autonomous multi-agent workflow execution system",
    version="1.0.0",
    lifespan=lifespan
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(workflows.router, prefix="/api/workflows", tags=["workflows"])
app.include_router(agents.router, prefix="/api/agents", tags=["agents"])
app.include_router(tools.router, prefix="/api/tools", tags=["tools"])
app.include_router(executions.router, prefix="/api/executions", tags=["executions"])


@app.get("/")
async def root():
    return {
        "message": "Agentic Workflow Manager API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
