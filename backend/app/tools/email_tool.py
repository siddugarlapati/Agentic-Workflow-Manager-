from langchain.tools import BaseTool
import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config import settings


class SendEmailTool(BaseTool):
    name = "send_email"
    description = "Send an email to a recipient"
    
    def _run(self, to_email: str, subject: str, body: str, html: bool = False) -> str:
        """Send email (sync wrapper)"""
        import asyncio
        return asyncio.run(self._arun(to_email, subject, body, html))
    
    async def _arun(self, to_email: str, subject: str, body: str, html: bool = False) -> str:
        """Send email"""
        if not settings.SMTP_USER or not settings.SMTP_PASSWORD:
            return "Email credentials not configured"
        
        try:
            message = MIMEMultipart("alternative")
            message["From"] = settings.SMTP_USER
            message["To"] = to_email
            message["Subject"] = subject
            
            if html:
                message.attach(MIMEText(body, "html"))
            else:
                message.attach(MIMEText(body, "plain"))
            
            await aiosmtplib.send(
                message,
                hostname=settings.SMTP_HOST,
                port=settings.SMTP_PORT,
                username=settings.SMTP_USER,
                password=settings.SMTP_PASSWORD,
                start_tls=True
            )
            
            return f"Email sent to {to_email}"
        except Exception as e:
            return f"Error sending email: {str(e)}"
