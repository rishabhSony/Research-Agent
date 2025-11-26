# Multi-Agent Research Assistant 🕵️‍♂️

**Autonomous Research & Synthesis System**

A sophisticated multi-agent system designed to conduct deep web research, synthesize information from diverse sources, and generate citation-backed reports. Built on the **LangChain** framework, it employs a hierarchical agent architecture to ensure accuracy and reduce hallucination.

## 🧠 System Architecture

The system operates using a coordinator-worker pattern:

1.  **Planner Agent**: Decomposes the user's high-level query into specific research sub-tasks.
2.  **Researcher Agent**: Executes targeted web searches using the **Tavily API**, filtering for high-authority domains.
3.  **Analyst Agent**: Cross-references gathered data to verify facts and identify contradictions.
4.  **Writer Agent**: Synthesizes the verified information into a structured Markdown report with inline citations.

## 🚀 Key Features

-   **Hierarchical Task Decomposition**: Breaks down complex topics (e.g., "Future of Quantum Computing") into manageable research vectors.
-   **Anti-Hallucination Protocol**: Cross-verification step ensures all claims are backed by at least two independent sources.
-   **Real-time Web Access**: Accesses live data, bypassing the knowledge cutoff limitations of static LLMs.
-   **Streamlit Interface**: Interactive UI for monitoring agent thought processes and intermediate outputs.

## 🛠️ Tech Stack

-   **Orchestration**: LangChain, LangGraph
-   **LLM**: Google Gemini 1.5 Pro / GPT-4 Turbo
-   **Search**: Tavily Search API
-   **Frontend**: Streamlit
-   **Environment**: Python 3.10+

## 📦 Installation

```bash
git clone https://github.com/rishabhSony/Research-Agent.git
cd Research-Agent
pip install -r requirements.txt
```

## 🏃‍♂️ Usage

```bash
streamlit run app.py
```

## 📄 License
MIT License
