import os
import sendgrid
from agents import Agent, function_tool
from sendgrid.helpers.mail import Email, To, Content, Mail
from model_setup import gemini_model

@function_tool
def send_email(html_body: str, subject: str) -> dict:
    """Send a research report via SendGrid."""
    import os
    import sendgrid
    from sendgrid.helpers.mail import Email, To, Content, Mail

    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
    from_email = Email("deepnagpal147514@gmail.com")  # verified
    to_email = To(os.environ.get("USER_EMAIL"))       # recipient email
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    response = sg.client.mail.send.post(request_body=mail)
    return {"status": "success" if response.status_code == 202 else "failed", "code": response.status_code}


email_instructions = """
You are an AI that converts a detailed research report into a nicely formatted HTML email.
You will be provided with the HTML report and a subject line.

Requirements:
1. Use the provided subject line for the email.
2. Include sections for Introduction, Analysis, Case Studies, etc.
3. Style key points using inline CSS.
4. Output valid HTML suitable for sending via email.
"""
email_agent = Agent(
    name="Email Agent",
    instructions=email_instructions,
    tools=[send_email],
    model=gemini_model
)
