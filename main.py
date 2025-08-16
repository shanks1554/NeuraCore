import gradio as gr
import asyncio
from research_manager import ResearchManager
import markdown

manager = ResearchManager()

def run_research(query, email):
    async def _run():
        report = await manager.run(query, email)
        html_report = markdown.markdown(report.markdown_report)
        return html_report
    return asyncio.run(_run())

with gr.Blocks() as demo:
    # Inject custom CSS
    gr.HTML(
        """
        <style>
        #report_output {
            height: 600px;
            width: 100%;
            overflow: auto;
            border: 1px solid #ccc;
            padding: 10px;
        }
        #run_btn {
            background-color: #2563eb;  /* Tailwind blue-600 */
            color: white;
            font-size: 16px;
            font-weight: 600;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        #run_btn:hover {
            background-color: #1d4ed8;  /* darker blue on hover */
        }
        </style>
        """
    )
    
    gr.Markdown("# NeuraCore: Your AI Research Assistant")
    
    query_input = gr.Textbox(label="Enter Research Topic")
    email_input = gr.Textbox(label="Enter Your Email")
    run_btn = gr.Button("Generate Report",elem_id = "run_btn")
    # Use gr.HTML with elem_id
    output_display = gr.HTML(
        label="Generated Report",
        elem_id="report_output",
        value=""
    )
    run_btn.click(fn=run_research, inputs=[query_input, email_input], outputs=output_display)

demo.launch(inbrowser=True)