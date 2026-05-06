from app.tools.jira_tool import JiraCreateProjectTool, JiraCreateIssueTool
from app.tools.stripe_tool import StripeCreateCustomerTool, StripeCreateSubscriptionTool
from app.tools.email_tool import SendEmailTool


def get_available_tools():
    """Get all available tools for agents"""
    return [
        JiraCreateProjectTool(),
        JiraCreateIssueTool(),
        StripeCreateCustomerTool(),
        StripeCreateSubscriptionTool(),
        SendEmailTool()
    ]


def get_tool_by_name(tool_name: str):
    """Get a specific tool by name"""
    tools = get_available_tools()
    for tool in tools:
        if tool.name == tool_name:
            return tool
    return None
