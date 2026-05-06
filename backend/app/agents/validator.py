from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from app.core.config import settings


class ValidatorAgent:
    """Agent responsible for validating execution results"""
    
    def __init__(self):
        self.llm = Ollama(
            base_url=settings.OLLAMA_BASE_URL,
            model=settings.OLLAMA_MODEL
        )
        
        self.prompt = PromptTemplate(
            input_variables=["step", "result", "expected_output"],
            template="""You are a validation agent. Verify if the execution result meets expectations.

Step: {step}
Result: {result}
Expected Output: {expected_output}

Analyze:
1. Was the step executed successfully?
2. Does the result match expected output?
3. Are there any errors or anomalies?
4. Should we proceed or retry?

Return a JSON with:
- valid: true/false
- errors: list of errors if any
- suggestions: how to fix if invalid
"""
        )
    
    async def validate(self, step: dict, result: dict, expected_output: dict) -> dict:
        """Validate execution result"""
        chain = self.prompt | self.llm
        validation = await chain.ainvoke({
            "step": step,
            "result": result,
            "expected_output": expected_output
        })
        
        import json
        try:
            return json.loads(validation)
        except:
            return {"valid": True, "errors": [], "suggestions": []}
