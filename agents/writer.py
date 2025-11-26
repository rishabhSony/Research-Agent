from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from utils.config import Config

class WriterAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model=Config.MODEL_NAME, temperature=0.7, google_api_key=Config.GOOGLE_API_KEY)
        
        self.prompt = ChatPromptTemplate.from_template(
            """
            You are a professional technical writer. Your task is to write a comprehensive report based on the research findings provided below.

            Topic: {topic}
            
            Research Findings:
            {research_summary}

            Format the report in Markdown with the following structure:
            # Title
            ## Executive Summary
            ## Key Findings
            ## Detailed Analysis
            ## Conclusion

            Make the report engaging, professional, and easy to read.
            """
        )

    def write_report(self, topic: str, research_summary: str) -> str:
        print(f"✍️  Writing report for: {topic}...")
        
        chain = self.prompt | self.llm | StrOutputParser()
        report = chain.invoke({
            "topic": topic,
            "research_summary": research_summary
        })
        
        return report
