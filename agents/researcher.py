from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from utils.config import Config

class ResearcherAgent:
    def __init__(self):
        self.search_tool = TavilySearchResults(max_results=5)
        self.llm = ChatOpenAI(model=Config.MODEL_NAME, temperature=0)
        
        self.prompt = ChatPromptTemplate.from_template(
            """
            You are an expert researcher. Your goal is to find detailed and accurate information about the following topic:
            {topic}

            Use the search results provided below to answer the user's request. 
            Focus on finding facts, statistics, and recent developments.
            
            Search Results:
            {search_results}

            Provide a comprehensive summary of the findings.
            """
        )

    def research(self, topic: str) -> str:
        print(f"🔎 Researching topic: {topic}...")
        
        # 1. Perform search
        try:
            search_results = self.search_tool.invoke({"query": topic})
        except Exception as e:
            return f"Error performing search: {str(e)}"

        # 2. Synthesize results using LLM
        chain = self.prompt | self.llm | StrOutputParser()
        summary = chain.invoke({
            "topic": topic,
            "search_results": str(search_results)
        })
        
        return summary
