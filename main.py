import argparse
import logging
import sys
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent
from utils.config import Config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def setup_args():
    parser = argparse.ArgumentParser(description="Multi-Agent Research Assistant")
    parser.add_argument("topic", nargs="*", help="The topic to research")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    return parser.parse_args()

def main():
    args = setup_args()
    
    if args.verbose:
        logger.setLevel(logging.DEBUG)

    try:
        Config.validate()
    except ValueError as e:
        logger.error(f"Configuration Error: {e}")
        logger.info("Please ensure .env file contains OPENAI_API_KEY and TAVILY_API_KEY")
        sys.exit(1)

    logger.info("Initializing Multi-Agent Research Assistant...")
    
    if args.topic:
        topic = " ".join(args.topic)
    else:
        try:
            topic = input("Enter a topic to research: ").strip()
        except KeyboardInterrupt:
            print("\n")
            logger.info("Exiting...")
            sys.exit(0)

    if not topic:
        logger.warning("No topic provided. Exiting.")
        sys.exit(0)

    try:
        # Initialize Agents
        researcher = ResearcherAgent()
        writer = WriterAgent()

        # Phase 1: Research
        logger.info(f"Starting research on: {topic}")
        research_summary = researcher.research(topic)
        
        # Phase 2: Writing
        logger.info("Synthesizing research into final report...")
        final_report = writer.write_report(topic, research_summary)

        # Output
        print("\n" + "="*50)
        print("FINAL REPORT")
        print("="*50 + "\n")
        print(final_report)
        
        # Save artifact
        filename = f"{topic.replace(' ', '_').lower()}_report.md"
        with open(filename, "w") as f:
            f.write(final_report)
        logger.info(f"Report saved successfully to {filename}")

    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
