from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class WorkflowCreate(BaseModel):
    name: str
    description: Optional[str] = None
    definition: Dict[Any, Any]
    created_by: Optional[str] = None


class WorkflowResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    status: str
    definition: Dict[Any, Any]
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True
