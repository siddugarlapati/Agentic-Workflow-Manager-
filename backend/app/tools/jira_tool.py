from langchain.tools import BaseTool
from jira import JIRA
from app.core.config import settings
from typing import Optional


class JiraCreateProjectTool(BaseTool):
    name = "jira_create_project"
    description = "Create a new project in Jira"
    
    def _run(self, project_key: str, project_name: str, lead_account_id: str) -> str:
        """Create Jira project"""
        if not settings.JIRA_URL or not settings.JIRA_API_TOKEN:
            return "Jira credentials not configured"
        
        try:
            jira = JIRA(
                server=settings.JIRA_URL,
                basic_auth=(settings.JIRA_EMAIL, settings.JIRA_API_TOKEN)
            )
            
            project = jira.create_project(
                key=project_key,
                name=project_name,
                lead=lead_account_id,
                template_name="com.pyxis.greenhopper.jira:gh-simplified-scrum"
            )
            
            return f"Project created: {project.key} - {project.name}"
        except Exception as e:
            return f"Error creating project: {str(e)}"
    
    async def _arun(self, *args, **kwargs):
        return self._run(*args, **kwargs)


class JiraCreateIssueTool(BaseTool):
    name = "jira_create_issue"
    description = "Create a new issue in Jira"
    
    def _run(self, project_key: str, summary: str, description: str, issue_type: str = "Task") -> str:
        """Create Jira issue"""
        if not settings.JIRA_URL or not settings.JIRA_API_TOKEN:
            return "Jira credentials not configured"
        
        try:
            jira = JIRA(
                server=settings.JIRA_URL,
                basic_auth=(settings.JIRA_EMAIL, settings.JIRA_API_TOKEN)
            )
            
            issue = jira.create_issue(
                project=project_key,
                summary=summary,
                description=description,
                issuetype={"name": issue_type}
            )
            
            return f"Issue created: {issue.key}"
        except Exception as e:
            return f"Error creating issue: {str(e)}"
    
    async def _arun(self, *args, **kwargs):
        return self._run(*args, **kwargs)
