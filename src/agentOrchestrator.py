import json
import sys
import os
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_groq import ChatGroq
from contentExtraction import extract_content_from_url  
from summarize import summarize_text  
from webSearch import search_related_content

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from contentExtraction import extract_content_from_url  # type: ignore
from summarize import summarize_text  # type: ignore
from webSearch import search_related_content  # type: ignore
from generateTwitterPost import generate_twitter_post  # type: ignore
from postOnTwitter import ask_to_post  # type: ignore
from googleSheetUpdate import update_google_sheet # type: ignore

# Load configuration from JSON file
with open('config/config.json', 'r') as f:
    config = json.load(f)
    groq_api_key = config.get('groq_api_key')
    print(f"Loaded API key: {groq_api_key}")

# Define the tools for the agent
def content_extraction_tool(url: str) -> str:
    """Tool for extracting content from a URL."""
    content = extract_content_from_url(url)
    if not content:
        return "Failed to extract content. Ensure the URL is valid and accessible."
    return content

def summarization_tool(content: str) -> str:
    """Tool for summarizing extracted content."""
    summary = summarize_text(content)
    if not summary:
        return "Failed to summarize content."
    return summary

def web_search_tool(query: str) -> str:
    """Tool for searching related content on the web."""
    search_results = search_related_content(query)
    if not search_results:
        return "No related content found."
    # Combine search results into a single string for simplicity
    combined_results = "\n".join([f"{result['title']}: {result['link']}" for result in search_results])
    return combined_results

def related_content_processing_tool(query: str) -> str:
    """Tool for extracting and summarizing content from related URLs."""
    search_results = search_related_content(query)
    if not search_results:
        return "No related content found to process."

    processed_results = []
    for result in search_results:
        url = result.get('link')
        if not url:
            continue
        # Extract and summarize content from the related URL
        content = extract_content_from_url(url)
        if content:
            summary = summarize_text(content)
            processed_results.append({
                "title": result.get('title'),
                "url": url,
                "summary": summary or "Failed to summarize content."
            })

    if not processed_results:
        return "Failed to process related URLs."

    # Combine results into a readable string
    output = "\n".join([
        f"Title: {item['title']}\nURL: {item['url']}\nSummary: {item['summary']}\n"
        for item in processed_results
    ])
    return output

# Initialize the agent with tools
def create_agent():
    # Initialize the Groq model with the API key
    chat = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768", api_key=groq_api_key)

    # Define the tools for the agent
    tools = [
        Tool(
            name="Content Extraction",
            func=content_extraction_tool,
            description="Extract content from a given URL."
        ),
        Tool(
            name="Summarization",
            func=summarization_tool,
            description="Summarize the provided content."
        ),
        Tool(
            name="Web Search",
            func=web_search_tool,
            description="Search for related content based on the query."
        ),
        Tool(
            name="Related Content Processing",
            func=related_content_processing_tool,
            description="Extract and summarize content from related URLs found in a web search."
        ),
    ]

    # Initialize LangChain agent with tools and Groq API model (chat)
    agent = initialize_agent(
        tools=tools,
        llm=chat,  # Use the Groq model here
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True  # Enable verbose logging for debugging
    )

    return agent

def run_agent(url: str):
    """Run the agent to process the URL."""
    agent = create_agent()
    print(f"Processing URL: {url}")
    # Run the agent and return the result
    result = agent.run(f"Extract content from this URL, summarize it, and search for related content: {url}")
    return result

if __name__ == "__main__":
    # Input URL for testing
    test_url = "https://brandequity.economictimes.indiatimes.com/news/digital/code-is-dead-outcomes-is-king-why-ai-is-driving-software-industrys-biggest-disruption/117280810" 
    result = run_agent(test_url)
    print("\nAgent Result:\n")
    print(result)
