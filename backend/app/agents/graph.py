from typing import TypedDict, Annotated, Sequence
from langgraph.graph import StateGraph, END
from langchain_core.messages import BaseMessage
import operator


class AgentState(TypedDict):
    """State shared across all agents in the workflow"""
    messages: Annotated[Sequence[BaseMessage], operator.add]
    workflow_id: int
    execution_id: int
    current_step: int
    steps: list
    context: dict
    errors: list
    retry_count: int
    max_retries: int


def create_workflow_graph():
    """Create the LangGraph workflow with multiple agents"""
    
    workflow = StateGraph(AgentState)
    
    # Add nodes (agents)
    workflow.add_node("planner", planner_agent)
    workflow.add_node("executor", executor_agent)
    workflow.add_node("validator", validator_agent)
    workflow.add_node("corrector", corrector_agent)
    
    # Define edges
    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "executor")
    workflow.add_conditional_edges(
        "executor",
        should_validate,
        {
            "validate": "validator",
            "end": END
        }
    )
    workflow.add_conditional_edges(
        "validator",
        validation_result,
        {
            "success": END,
            "retry": "corrector",
            "fail": END
        }
    )
    workflow.add_edge("corrector", "executor")
    
    return workflow.compile()


def planner_agent(state: AgentState) -> AgentState:
    """Plans the workflow execution steps"""
    # Implementation in planner.py
    pass


def executor_agent(state: AgentState) -> AgentState:
    """Executes workflow steps using tools"""
    # Implementation in executor.py
    pass


def validator_agent(state: AgentState) -> AgentState:
    """Validates execution results"""
    # Implementation in validator.py
    pass


def corrector_agent(state: AgentState) -> AgentState:
    """Corrects errors and retries"""
    # Implementation in corrector.py
    pass


def should_validate(state: AgentState) -> str:
    """Decide if validation is needed"""
    if state["current_step"] >= len(state["steps"]):
        return "end"
    return "validate"


def validation_result(state: AgentState) -> str:
    """Route based on validation result"""
    if not state["errors"]:
        return "success"
    if state["retry_count"] < state["max_retries"]:
        return "retry"
    return "fail"
