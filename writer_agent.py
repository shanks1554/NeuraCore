from pydantic import BaseModel, Field
from agents import Agent
from model_setup import gemini_model

class ReportSection(BaseModel):
    section_title: str
    section_content: str

class ReportData(BaseModel):
    short_summary: str
    markdown_report: str
    sections: list[ReportSection]
    follow_up_questions: list[str]

writer_instructions = """
You are a senior research assistant tasked with writing a detailed section of a research report.
You will be provided with:
- The research query
- Detailed research summaries collected from multiple web searches
- Section title to write

Requirements:
1. Write content only for the specified section.
2. Make it detailed, including examples, tables, statistics, or frameworks where relevant.
3. Output must be in Markdown format.
4. Avoid personal opinions; base content on the research summaries.
5. The final report will be built by combining all sections. Do not generate the full report here.
"""

writer_agent = Agent(
    name="Writer Agent",
    instructions=writer_instructions,
    model=gemini_model,
    output_type=ReportSection
)