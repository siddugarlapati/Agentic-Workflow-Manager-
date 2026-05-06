from langchain_community.llms import Ollama
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from app.core.config import settings
from app.tools.registry import get_available_tools


class ExecutorAgent:
    """Agent responsible for executing workflow steps"""
    
    def __init__(self):
        self.llm = Ollama(
            base_url=settings.OLLAMA_BASE_URL,
            model=settings.OLLAMA_MODEL
        )
        
        self.prompt = PromptTemplate.from_template("""
You are a workflow execution agent. Execute the given step using available tools.

Step: {step}
Context: {context}

Available tools: {tools}

Think step by step:
1. What tool(s) do I need?
2. What parameters are required?
3. Execute the tool
4. Verify the result

{agent_scratchpad}
""")
    
    async def execute_step(self, step: dict, context: dict) -> dict:
        """Execute a single workflow step"""
        tools = get_available_tools()
        
        agent = create_react_agent(self.llm, tools, self.prompt)
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            verbose=True,
            max_iterations=5
        )
        
        result = await agent_executor.ainvoke({
            "step": step,
            "context": context
        })
        
        return result
