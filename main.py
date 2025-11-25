import sys
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent
from utils.config import Config

def main():
    try:
        # Validate environment variables
        Config.validate()
    except ValueError as e:
        print(f"❌ Configuration Error: {e}")
        print("Please create a .env file with OPENAI_API_KEY and TAVILY_API_KEY")
        return

    print("🤖 Multi-Agent Research Assistant Initialized")
    print("---------------------------------------------")
    
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
    else:
        topic = input("Enter a topic to research: ")

    if not topic:
        print("❌ No topic provided. Exiting.")
        return

    # Initialize Agents
    researcher = ResearcherAgent()
    writer = WriterAgent()

    # Step 1: Research
    print("\n--- Step 1: Gathering Information ---")
    research_summary = researcher.research(topic)
    
    # Step 2: Write Report
    print("\n--- Step 2: Generating Report ---")
    final_report = writer.write_report(topic, research_summary)

    # Output Result
    print("\n\n" + "="*50)
    print("FINAL REPORT")
    print("="*50 + "\n")
    print(final_report)
    
    # Save to file
    filename = f"{topic.replace(' ', '_').lower()}_report.md"
    with open(filename, "w") as f:
        f.write(final_report)
    print(f"\n\n✅ Report saved to {filename}")

if __name__ == "__main__":
    main()
