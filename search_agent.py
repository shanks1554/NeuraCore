from agents import Agent, function_tool, ModelSettings
from model_setup import gemini_model
import os
import requests

# Decorate the search function
@function_tool
def google_search(query: str) -> str:
    """Search the web and return top 5 results as text."""
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
    url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": GOOGLE_API_KEY, "cx": GOOGLE_CSE_ID, "q": query, "num": 5}

    try:
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()
        results = []
        for item in data.get("items", []):
            results.append(f"{item.get('title')}: {item.get('snippet')} ({item.get('link')})")
        return "\n".join(results)
    except Exception as e:
        return f"Google search failed: {e}"

# Create the agent
search_instructions = """
You are a research assistant AI. Given a topic, search the web and produce a structured summary capturing all key points and insights.

Rules:
1. Summarize in 3-5 paragraphs or bullet points.
2. Include relevant facts, trends, frameworks, or technologies.
3. Focus on authoritative sources and recent information (2020+ if applicable).
4. Include references or links for key information.
5. Present findings clearly; no fluff or personal opinions.
6. Output should be readable and suitable for use in a detailed research report.

"""

search_agent = Agent(
    name="Deep Research Agent",
    instructions=search_instructions,
    model=gemini_model,
    tools=[google_search],  # just the decorated function
    model_settings=ModelSettings(tool_choice="required")
)
