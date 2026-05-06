from sqlalchemy import Column, Integer, String, Text, DateTime, JSON, ForeignKey
from sqlalchemy.sql import func
from app.db.database import Base


class AgentMemory(Base):
    """Long-term memory for agents"""
    __tablename__ = "agent_memory"
    
    id = Column(Integer, primary_key=True, index=True)
    execution_id = Column(Integer, ForeignKey("workflow_executions.id"))
    agent_name = Column(String(255), nullable=False)
    
    # Memory content
    memory_type = Column(String(50))  # episodic, semantic, procedural
    content = Column(JSON, nullable=False)
    
    # Context
    context = Column(JSON)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    relevance_score = Column(Integer, default=0)
