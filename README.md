# 🔬 ResearchMind - Multi-Agent AI Research System

ResearchMind is a multi-agent AI research platform built using **LangChain**, **Gemini**, **Tavily Search**, **BeautifulSoup**, and **Streamlit**.

The system automates the complete research workflow by employing specialized AI agents that collaborate to:

* Search the web for relevant information
* Extract content from authoritative sources
* Generate detailed research reports
* Critique and evaluate the generated report

## 🚀 Live Demo

https://multiresearch-agent-system.streamlit.app/

## ✨ Features

* Multi-Agent Architecture
* Web Search using Tavily
* Web Scraping using BeautifulSoup
* Research Report Generation
* Automated Critic & Feedback System
* Streamlit User Interface
* Modular LangChain Agent Design
* Gemini-powered LLM Integration

## 🏗️ Architecture

```text
User Query
    │
    ▼
Search Agent
(Tavily Search)
    │
    ▼
Reader Agent
(Web Scraping)
    │
    ▼
Writer Chain
(Report Generation)
    │
    ▼
Critic Chain
(Quality Evaluation)
    │
    ▼
Final Research Report
```

## 🛠️ Tech Stack

* Python
* LangChain
* Gemini API
* Tavily Search API
* BeautifulSoup
* Streamlit
* Rich
* Requests
* Pydantic

## 📂 Project Structure

```text
Multi Agent System
│
├── agents.py
├── tools.py
├── pipeline.py
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
```

## ▶️ Run Locally

```bash
streamlit run app.py
```

## ⚠️ API Key Notice

The deployed version currently uses the Gemini Free Tier API. The available quota may become exhausted, causing the application to temporarily stop generating responses.

If you fork or run this project locally, you can easily switch to any supported LLM provider, including:

* Gemini
* OpenAI
* Groq
* Mistral
* Anthropic Claude
* Together AI
* Ollama (Local Models)

Only minor changes in the LLM initialization code are required.

## 🔮 Future Improvements

* LangGraph-based orchestration
* Multi-source scraping
* PDF report export
* Research memory and persistence
* Citation tracking
* Agent monitoring and observability

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

## 📜 License

This project is open-source and available under the MIT License.
