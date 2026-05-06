from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
async def get_agents_status():
    """Get status of all agents"""
    return {
        "agents": [
            {"name": "planner", "status": "active"},
            {"name": "executor", "status": "active"},
            {"name": "validator", "status": "active"},
            {"name": "corrector", "status": "active"}
        ]
    }


@router.get("/memory/{execution_id}")
async def get_agent_memory(execution_id: int):
    """Get agent memory for an execution"""
    # TODO: Implement memory retrieval
    return {"execution_id": execution_id, "memory": []}
