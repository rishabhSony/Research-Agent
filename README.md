# Multi-Agent Research Assistant

An autonomous AI system that coordinates multiple specialized agents to conduct comprehensive research, synthesize findings, and generate detailed reports.

## 🚀 Features

-   **Autonomous Research**: Uses Tavily Search API to find real-time information on any topic.
-   **Multi-Agent Architecture**:
    -   **Researcher Agent**: Gathers facts, statistics, and recent developments.
    -   **Writer Agent**: Synthesizes information into a professional markdown report.
-   **LangChain Integration**: Built using the latest LangChain primitives for robust agent orchestration.

## 🛠️ Prerequisites

-   Python 3.8+
-   OpenAI API Key
-   Tavily API Key (Get one for free at [tavily.com](https://tavily.com))

## 📦 Installation

1.  **Clone the repository**:
    ```bash
    git clone git@github.com:rishabhSony/Research-Agent.git
    cd Research-Agent
    ```

2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**:
    Create a `.env` file in the root directory:
    ```bash
    touch .env
    ```
    Add your API keys:
    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    TAVILY_API_KEY=your_tavily_api_key_here
    MODEL_NAME=gpt-4-turbo-preview
    ```

## 🏃‍♂️ Usage

Run the main script and follow the prompts:

```bash
python main.py
```

Or provide a topic directly as an argument:

```bash
python main.py "The future of Generative AI in Healthcare"
```

## 📂 Project Structure

```
Research-Agent/
├── agents/
│   ├── researcher.py  # Handles web search and fact-gathering
│   └── writer.py      # Synthesizes findings into a report
├── utils/
│   └── config.py      # Configuration and environment management
├── main.py            # Entry point
├── requirements.txt   # Python dependencies
└── README.md          # Documentation
```

## 📝 Example Output

The system generates a markdown file (e.g., `generative_ai_in_healthcare_report.md`) containing:

-   **Executive Summary**: High-level overview.
-   **Key Findings**: Bullet points of critical information.
-   **Detailed Analysis**: In-depth exploration of the topic.
-   **Conclusion**: Final thoughts and future outlook.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.
