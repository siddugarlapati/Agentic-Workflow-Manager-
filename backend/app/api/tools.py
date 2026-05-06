from fastapi import APIRouter
from app.tools.registry import get_available_tools

router = APIRouter()


@router.get("/")
async def list_tools():
    """List all available tools"""
    tools = get_available_tools()
    return {
        "tools": [
            {
                "name": tool.name,
                "description": tool.description
            }
            for tool in tools
        ]
    }


@router.get("/{tool_name}")
async def get_tool_info(tool_name: str):
    """Get information about a specific tool"""
    from app.tools.registry import get_tool_by_name
    tool = get_tool_by_name(tool_name)
    if not tool:
        return {"error": "Tool not found"}
    
    return {
        "name": tool.name,
        "description": tool.description
    }
