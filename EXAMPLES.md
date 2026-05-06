# Usage Examples

## Example 1: Client Onboarding Workflow

This workflow automates the complete client onboarding process.

### Create the Workflow

```bash
curl -X POST http://localhost:8000/api/workflows \
  -H "Content-Type: application/json" \
  -d @backend/app/templates/client_onboarding.json
```

### Execute the Workflow

```bash
curl -X POST http://localhost:8000/api/executions \
  -H "Content-Type: application/json" \
  -d '{
    "workflow_id": 1,
    "input_data": {
      "client_name": "Acme Corp",
      "client_email": "contact@acme.com",
      "client_code": "ACME",
      "project_lead_id": "user123",
      "subscription_plan_id": "price_1234"
    }
  }'
```

### What Happens

1. **Planner Agent** analyzes the workflow and creates execution plan
2. **Executor Agent** performs these actions:
   - Creates Jira project "ACME"
   - Creates initial setup tasks
   - Creates Stripe customer
   - Sets up subscription
   - Sends welcome email
3. **Validator Agent** checks each step's result
4. **Corrector Agent** retries if any step fails

### Monitor Execution

```bash
# Get execution status
curl http://localhost:8000/api/executions/1

# Response
{
  "id": 1,
  "status": "completed",
  "trace": [
    {"step": 1, "action": "jira_create_project", "result": "Project created: ACME"},
    {"step": 2, "action": "jira_create_issue", "result": "Issue created: ACME-1"},
    ...
  ]
}
```

## Example 2: Custom Workflow - Invoice Processing

### Workflow Definition

```json
{
  "name": "Invoice Processing",
  "description": "Process and validate invoices",
  "steps": [
    {
      "id": 1,
      "name": "Extract Invoice Data",
      "tool": "ocr_extract",
      "parameters": {
        "document_url": "{{invoice_url}}"
      }
    },
    {
      "id": 2,
      "name": "Validate Data",
      "tool": "validate_invoice",
      "parameters": {
        "invoice_data": "{{step_1_result}}"
      }
    },
    {
      "id": 3,
      "name": "Create Payment",
      "tool": "stripe_create_payment",
      "parameters": {
        "amount": "{{step_1_result.total}}",
        "customer_id": "{{customer_id}}"
      }
    },
    {
      "id": 4,
      "name": "Send Confirmation",
      "tool": "send_email",
      "parameters": {
        "to_email": "{{vendor_email}}",
        "subject": "Payment Processed",
        "body": "Payment of {{step_1_result.total}} has been processed."
      }
    }
  ]
}
```

## Example 3: Self-Correction in Action

### Scenario: Failed Jira Project Creation

```
1. Executor tries to create project with key "TEST-123"
2. Jira returns error: "Invalid project key format"
3. Validator detects failure
4. Validator suggests: "Remove hyphens from project key"
5. Corrector updates parameters: key = "TEST123"
6. Executor retries with corrected key
7. Success!
```

### Execution Trace

```json
{
  "trace": [
    {
      "step": 1,
      "attempt": 1,
      "action": "jira_create_project",
      "parameters": {"project_key": "TEST-123"},
      "result": "Error: Invalid project key format",
      "validation": {
        "valid": false,
        "errors": ["Invalid key format"],
        "suggestions": ["Remove special characters"]
      }
    },
    {
      "step": 1,
      "attempt": 2,
      "action": "jira_create_project",
      "parameters": {"project_key": "TEST123"},
      "result": "Project created: TEST123",
      "validation": {"valid": true}
    }
  ]
}
```

## Example 4: Using the Frontend

### 1. View Dashboard
Navigate to `http://localhost:5173` to see execution statistics.

### 2. Create Workflow
- Click "Workflows" in navigation
- Click "New Workflow" button
- Fill in workflow details
- Define steps and tools

### 3. Execute Workflow
- Select a workflow from the list
- Click "Execute" button
- Provide input parameters
- Monitor execution in real-time

### 4. View Results
- Go to "Executions" page
- Click on an execution to see details
- View execution trace
- Check agent decisions

## Example 5: Adding Custom Tools

### Create a Custom Tool

```python
# backend/app/tools/custom_tool.py
from langchain.tools import BaseTool

class CustomAPITool(BaseTool):
    name = "custom_api_call"
    description = "Call a custom API endpoint"
    
    def _run(self, endpoint: str, data: dict) -> str:
        import requests
        response = requests.post(endpoint, json=data)
        return response.json()
    
    async def _arun(self, *args, **kwargs):
        return self._run(*args, **kwargs)
```

### Register the Tool

```python
# backend/app/tools/registry.py
from app.tools.custom_tool import CustomAPITool

def get_available_tools():
    return [
        # ... existing tools
        CustomAPITool()
    ]
```

### Use in Workflow

```json
{
  "steps": [
    {
      "name": "Call Custom API",
      "tool": "custom_api_call",
      "parameters": {
        "endpoint": "https://api.example.com/action",
        "data": {"key": "value"}
      }
    }
  ]
}
```

## Testing

### Run Backend Tests

```bash
cd backend
pytest tests/ -v
```

### Test Individual Tools

```python
from app.tools.jira_tool import JiraCreateProjectTool

tool = JiraCreateProjectTool()
result = tool._run(
    project_key="TEST",
    project_name="Test Project",
    lead_account_id="user123"
)
print(result)
```
