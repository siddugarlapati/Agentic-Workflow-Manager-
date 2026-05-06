from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import datetime
from app.models.execution import WorkflowExecution, ExecutionStatus
from app.agents.planner import PlannerAgent
from app.agents.executor import ExecutorAgent
from app.agents.validator import ValidatorAgent


class WorkflowService:
    """Service for executing workflows with agents"""
    
    def __init__(self, db: AsyncSession):
        self.db = db
        self.planner = PlannerAgent()
        self.executor = ExecutorAgent()
        self.validator = ValidatorAgent()
    
    async def execute_workflow(
        self,
        execution_id: int,
        workflow_definition: dict,
        input_data: dict
    ):
        """Execute a workflow with multi-agent system"""
        try:
            # Update status to running
            result = await self.db.execute(
                select(WorkflowExecution).where(WorkflowExecution.id == execution_id)
            )
            execution = result.scalar_one()
            execution.status = ExecutionStatus.RUNNING
            await self.db.commit()
            
            # Step 1: Plan
            steps = await self.planner.plan(workflow_definition, input_data)
            
            # Step 2: Execute each step
            context = {"input": input_data}
            trace = []
            
            for i, step in enumerate(steps):
                # Execute
                result = await self.executor.execute_step(step, context)
                trace.append({
                    "step": i,
                    "action": step,
                    "result": result
                })
                
                # Validate
                validation = await self.validator.validate(
                    step, result, step.get("expected_output", {})
                )
                
                if not validation.get("valid", True):
                    # Self-correction: retry with suggestions
                    if validation.get("suggestions"):
                        step["corrections"] = validation["suggestions"]
                        result = await self.executor.execute_step(step, context)
                
                # Update context
                context[f"step_{i}_result"] = result
            
            # Update execution with results
            execution.status = ExecutionStatus.COMPLETED
            execution.output_data = context
            execution.trace = trace
            execution.completed_at = datetime.utcnow()
            await self.db.commit()
            
        except Exception as e:
            # Handle errors
            execution.status = ExecutionStatus.FAILED
            execution.error_message = str(e)
            execution.completed_at = datetime.utcnow()
            await self.db.commit()
