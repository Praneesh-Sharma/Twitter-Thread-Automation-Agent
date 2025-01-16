import json

from contentExtraction import extract_content_from_url  
from summarize import summarize_text  
from webSearch import search_related_content  

with open('config/config.json', 'r') as f:
    config = json.load(f)
    groq_api_key = config.get('groq_api_key')
    print(groq_api_key)


def content_extraction_tool(url: str) -> str:
    """Tool for extracting content from a URL."""
    return extract_content_from_url(url)

def summarization_tool(content: str) -> str:
    """Tool for summarizing extracted content."""
    return summarize_text(content)

def web_search_tool(query: str) -> list:
    """Tool for searching related content on the web."""
    return search_related_content(query)

def create_agent():
    """Create and initialize the LangChain agent."""
    # Pass the Gemini API key directly to the GeminiLM initialization
    # llm = GeminiLM(api_key=gemini_api_key)  # Pass the API key here
    chat = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768", api_key=groq_api_key)

    tools = [
        Tool(
            name="Content Extraction",
            func=content_extraction_tool,
            description="Extract content from a URL"
        ),
        Tool(
            name="Summarization",
            func=summarization_tool,
            description="Summarize the extracted content"
        ),
        Tool(
            name="Web Search",
            func=web_search_tool,
            description="Search for related content on the web"
        ),
    ]

    # Initialize LangChain agent with tools and LLM (Gemini API)
    agent = initialize_agent(
        tools=tools,
        llm=llm,  # Use the GeminiLM here
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True  # Enable verbose logging to debug issues
    )

    return agent

def run_agent(url: str):
    """Run the agent to process the URL."""
    agent = create_agent()
    # Run the agent and return the result (this will call all tools in sequence)
    return agent.run(url)

if __name__ == "__main__":
    # If you want to run the agent standalone with a URL input
    url = "https://blogs.nvidia.com/blog/ai-policy/"  # Replace with actual URL
    print(run_agent(url))
