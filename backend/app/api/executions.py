from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from datetime import datetime
from app.db.database import get_db
from app.models.execution import WorkflowExecution, ExecutionStatus
from app.models.workflow import Workflow
from app.schemas.execution import ExecutionCreate, ExecutionResponse
from app.services.workflow_service import WorkflowService

router = APIRouter()


@router.post("/", response_model=ExecutionResponse)
async def start_execution(
    execution: ExecutionCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    """Start a workflow execution"""
    # Verify workflow exists
    result = await db.execute(select(Workflow).where(Workflow.id == execution.workflow_id))
    workflow = result.scalar_one_or_none()
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    
    # Create execution record
    db_execution = WorkflowExecution(
        workflow_id=execution.workflow_id,
        input_data=execution.input_data,
        status=ExecutionStatus.PENDING,
        started_at=datetime.utcnow()
    )
    db.add(db_execution)
    await db.commit()
    await db.refresh(db_execution)
    
    # Execute workflow in background
    workflow_service = WorkflowService(db)
    background_tasks.add_task(
        workflow_service.execute_workflow,
        db_execution.id,
        workflow.definition,
        execution.input_data
    )
    
    return db_execution


@router.get("/{execution_id}", response_model=ExecutionResponse)
async def get_execution(execution_id: int, db: AsyncSession = Depends(get_db)):
    """Get execution status and results"""
    result = await db.execute(
        select(WorkflowExecution).where(WorkflowExecution.id == execution_id)
    )
    execution = result.scalar_one_or_none()
    if not execution:
        raise HTTPException(status_code=404, detail="Execution not found")
    return execution
