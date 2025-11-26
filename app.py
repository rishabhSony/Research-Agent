import streamlit as st
import os
from agents.researcher import ResearcherAgent
from agents.writer import WriterAgent
from utils.config import Config

# Page Configuration
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🕵️‍♂️",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
    }
    .report-container {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("🕵️‍♂️ Multi-Agent Research Assistant")
    st.markdown("---")

    # Sidebar for Configuration
    with st.sidebar:
        st.header("Configuration")
        
        # Check for API Keys
        google_key = os.getenv("GOOGLE_API_KEY")
        tavily_key = os.getenv("TAVILY_API_KEY")
        
        if not google_key or not tavily_key:
            st.warning("⚠️ API Keys missing! Please check your .env file.")
        else:
            st.success("✅ API Keys configured")
            
        st.markdown("### How it works")
        st.markdown("""
        1. **Researcher Agent**: Scours the web for real-time information.
        2. **Writer Agent**: Synthesizes findings into a professional report.
        """)

    # Main Content
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Research Topic")
        topic = st.text_area(
            "What would you like to research?",
            placeholder="e.g., The impact of Quantum Computing on Cybersecurity",
            height=150
        )
        
        start_btn = st.button("Start Research", type="primary")

    with col2:
        st.subheader("Research Report")
        report_container = st.empty()
        
        if start_btn and topic:
            if not google_key or not tavily_key:
                st.error("Please configure your API keys first.")
                return

            try:
                # Initialize Agents
                with st.spinner("Initializing Agents..."):
                    researcher = ResearcherAgent()
                    writer = WriterAgent()

                # Step 1: Research
                with st.status("🔍 Step 1: Gathering Information...", expanded=True) as status:
                    st.write("Searching the web for relevant data...")
                    research_summary = researcher.research(topic)
                    st.write("✅ Research complete!")
                    status.update(label="✅ Research Complete", state="complete", expanded=False)

                # Step 2: Writing
                with st.status("✍️ Step 2: Generating Report...", expanded=True) as status:
                    st.write("Synthesizing findings and writing report...")
                    final_report = writer.write_report(topic, research_summary)
                    status.update(label="✅ Report Generated", state="complete", expanded=False)

                # Display Report
                report_container.markdown(final_report)
                
                # Download Button
                st.download_button(
                    label="Download Report",
                    data=final_report,
                    file_name=f"{topic.replace(' ', '_').lower()}_report.md",
                    mime="text/markdown"
                )

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
