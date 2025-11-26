import logging
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from utils.config import Config

logger = logging.getLogger(__name__)

class ResearcherAgent:
    RESEARCH_PROMPT = """
    You are an expert researcher. Your goal is to find detailed and accurate information about the following topic:
    {topic}

    Use the search results provided below to answer the user's request. 
    Focus on finding facts, statistics, and recent developments.
    
    Search Results:
    {search_results}

    Provide a comprehensive summary of the findings.
    """

    def __init__(self):
        self.search_tool = TavilySearchResults(max_results=5)
        self.llm = ChatGoogleGenerativeAI(
            model=Config.MODEL_NAME, 
            temperature=0, 
            google_api_key=Config.GOOGLE_API_KEY
        )
        self.prompt = ChatPromptTemplate.from_template(self.RESEARCH_PROMPT)

    def research(self, topic: str) -> str:
        logger.info(f"Conducting research on: {topic}")
        
        try:
            # 1. Perform search
            search_results = self.search_tool.invoke({"query": topic})
            logger.debug(f"Search results found: {len(search_results)} items")
            
            # 2. Synthesize results using LLM
            chain = self.prompt | self.llm | StrOutputParser()
            summary = chain.invoke({
                "topic": topic,
                "search_results": str(search_results)
            })
            
            return summary
            
        except Exception as e:
            logger.error(f"Research failed: {str(e)}")
            raise RuntimeError(f"Failed to complete research on {topic}") from e
