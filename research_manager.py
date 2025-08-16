import asyncio
import markdown
from agents import Runner
from search_agent import search_agent
from planner_agent import planner_agent, WebSearchItem, WebSearchPlan
from writer_agent import writer_agent, ReportData, ReportSection
from email_agent import email_agent

class ResearchManager:

    sections_order = [
        "Introduction",
        "Background / Context",
        "Analysis / Insights",
        "Case Studies / Examples",
        "Challenges / Limitations",
        "Future Directions / Trends",
        "Conclusion"
    ]

    async def run(self, query: str, user_email: str):
        import os
        os.environ["USER_EMAIL"] = user_email  # dynamically set recipient email
        search_plan = await self.plan_searches(query)
        search_results = await self.perform_searches(search_plan)

        sections = []
        for section_title in self.sections_order:
            content = await self.write_section(query, search_results, section_title)
            sections.append(ReportSection(section_title=section_title, section_content=content))

        full_report = "\n\n".join([f"## {s.section_title}\n{s.section_content}" for s in sections])
        short_summary = sections[0].section_content[:200] + "..."  # first 200 chars as summary
        follow_up_questions = [f"Follow-up question {i+1}" for i in range(5)]

        report_data = ReportData(
            short_summary=short_summary,
            markdown_report=full_report,
            sections=sections,
            follow_up_questions=follow_up_questions
        )

        await self.send_email(report_data, query)
        return report_data

    async def plan_searches(self, query: str) -> WebSearchPlan:
        print("Planning...")
        result = await Runner.run(planner_agent, f"Query: {query}")
        return result.final_output_as(WebSearchPlan)

    async def perform_searches(self, search_plan: WebSearchPlan):
        print("Searching...")
        tasks = [asyncio.create_task(self.search(item)) for item in search_plan.searches]
        return await asyncio.gather(*tasks)

    async def search(self, item: WebSearchItem):
        result = await Runner.run(search_agent, f"Search term: {item.query}\nReason: {item.reason}")
        return str(result.final_output)

    async def write_section(self, query: str, search_results: list[str], section_title: str):
        print("Writing Report...")
        input_text = f"Query: {query}\nSearch summaries: {search_results}\nSection: {section_title}"
        result = await Runner.run(writer_agent, input_text)
        return result.final_output.section_content

    async def send_email(self, report: ReportData, query: str):
        print("Sending Email")
        html_body = markdown.markdown(report.markdown_report)
        await Runner.run(email_agent, f"Subject: Deep Research Report: {query}\nBody: {html_body}")
