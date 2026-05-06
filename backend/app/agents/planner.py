from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from app.core.config import settings
from app.agents.graph import AgentState


class PlannerAgent:
    """Agent responsible for planning workflow execution"""
    
    def __init__(self):
        self.llm = Ollama(
            base_url=settings.OLLAMA_BASE_URL,
            model=settings.OLLAMA_MODEL
        )
        
        self.prompt = PromptTemplate(
            input_variables=["workflow_definition", "input_data"],
            template="""You are a workflow planning agent. Given a workflow definition and input data,
create a detailed execution plan with specific steps.

Workflow Definition:
{workflow_definition}

Input Data:
{input_data}

Create a step-by-step execution plan. For each step, specify:
1. Action to perform
2. Tools required
3. Expected output
4. Dependencies on previous steps

Return the plan as a JSON array of steps."""
        )
    
    async def plan(self, workflow_definition: dict, input_data: dict) -> list:
        """Generate execution plan"""
        chain = self.prompt | self.llm
        result = await chain.ainvoke({
            "workflow_definition": workflow_definition,
            "input_data": input_data
        })
        
        # Parse and return steps
        import json
        try:
            steps = json.loads(result)
            return steps
        except:
            # Fallback: extract steps from workflow definition
            return workflow_definition.get("steps", [])
