from langchain.chains import LLMChain
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import BasePromptTemplate
# from langchain_community.agents import AgentExecutor
import json

from contentExtraction import extract_content_from_url  # type: ignore
from summarize import summarize_text  # type: ignore
from webSearch import search_related_content  # type: ignore

with open('config/config.json', 'r') as f:
    config = json.load(f)
    openai_api_key = config.get('openai_api_key')
    print(openai_api_key)


# Initialize LLM (Language Model)
llm = OpenAI(temperature=0.5, openai_api_key=openai_api_key)

# Define tools for LangChain Agent
tools = [
    Tool(
        name="content_extraction_tool",
        func=extract_content_from_url,
        description="Extracts relevant content from the URL"
    ),
    Tool(
        name="summarizer_tool",
        func=summarize_text,
        description="Summarizes the extracted content"
    ),
    Tool(
        name="web_search_tool",
        func=search_related_content,
        description="Searches for related content online"
    ),
]

# Initialize the agent with the tools defined
agent = initialize_agent(
    tools, llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# Define the AgentExecutor
def orchestrate_pipeline(url):
    result = agent.run(url)
    return result

if __name__ == "__main__":
    # User provides a URL, and the agent runs the complete pipeline
    url = input("Enter URL to process: ")
    result = orchestrate_pipeline(url)
    print("\nFinal Output:\n", result)
