import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "gemini-1.5-flash")

    @staticmethod
    def validate():
        if not Config.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")
        if not Config.TAVILY_API_KEY:
            raise ValueError("TAVILY_API_KEY not found in environment variables")
