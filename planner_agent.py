from pydantic import BaseModel, Field
from agents import Agent, function_tool
from model_setup import gemini_model

HOW_MANY_SEARCHES = 5

class WebSearchItem(BaseModel):
    reason: str
    query: str

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem]

planner_instructions = f"""
You are a research planning assistant. Given a research query and an initial summary, suggest 10-15 focused web searches to collect comprehensive information.

Rules:
1. Each search should include a clear reason for why it is important.
2. Ensure the combined searches cover all aspects of the topic (background, analysis, case studies, challenges, future directions).
3. Avoid overlap between searches.
4. These searches will be fed to the Search Agent for data collection.

"""

planner_agent = Agent(
    name="Planner Agent",
    instructions=planner_instructions,
    model=gemini_model,
    output_type=WebSearchPlan
)
