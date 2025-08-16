# 🧠 NeuraCore  
**An AI-powered Research Engine that thinks, organizes, and delivers insights with precision.**  

## 🚀 Overview  
NeuraCore is an intelligent, multi-agent research assistant that automates the end-to-end research process.  
Instead of spending hours searching, cross-checking, and note-taking — NeuraCore does the heavy lifting and delivers a **structured, multi-section research report** directly to your inbox.  

Built with the **OpenAI Agents SDK**, **Google Search API**, and a **clean Gradio UI**, NeuraCore brings together intelligent planning, data collection, and automated reporting in one seamless workflow.  

🔗 **Live Demo on Hugging Face:** [Try NeuraCore](https://deep1554-neuracore.hf.space/)  

---

## ✨ Features  
- 🔍 **Smart Research Planning** – Generates and refines queries for efficient exploration.  
- 🌐 **Web Insights Gathering** – Pulls and filters relevant information via Google Search API.  
- 📝 **Structured Report Writing** – Produces multi-section, well-formatted reports (Markdown → HTML).  
- 📧 **Email Delivery** – Sends a beautifully formatted copy of the report to your inbox.  
- 🎛 **Interactive UI** – User-friendly Gradio interface, deployed on Hugging Face.  

---

## 🛠 Tech Stack  
- **Python 3.12+**  
- **OpenAI Agents SDK** (for multi-agent orchestration)  
- **GEMINI Large Language Model**
- **Gradio** (for the interactive interface)  
- **Google Search API** (for real-time research data)  
- **SendGrid** (for email delivery)  

---

## 📦 Installation  

Clone the repo:  
```bash
git clone https://github.com/shanks1554/NeuraCore.git
cd NeuraCore
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Set up environment variables in .env:

```bash
GEMINI_API_KEY = Your Gemini API KEY

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

SENDGRID_API_KEY = Your SendGrid API KEY

GOOGLE_CSE_ID = Your Google Custom Search Engine ID

GOOGLE_API_KEY = Your Google API Key
```

## Run the app locally:

```bash
python main.py
```
## 🌐 Deployment

NeuraCore is deployed seamlessly on Hugging Face Spaces using Gradio.
You can fork this repo and deploy your own version:
```bash
gradio deploy .
```

## 📬 Demo

🔗 Live Hugging Face Demo: [NeuraCore on Hugging Face](https://deep1554-neuracore.hf.space/)

## 📜 License

This project is licensed under the MIT License.