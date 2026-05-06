from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from datetime import datetime


class ExecutionCreate(BaseModel):
    workflow_id: int
    input_data: Dict[Any, Any]


class ExecutionResponse(BaseModel):
    id: int
    workflow_id: int
    status: str
    input_data: Dict[Any, Any]
    trace: Optional[List[Dict[Any, Any]]] = []
    output_data: Optional[Dict[Any, Any]] = None
    error_message: Optional[str] = None
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    created_at: datetime
    
    class Config:
        from_attributes = True
