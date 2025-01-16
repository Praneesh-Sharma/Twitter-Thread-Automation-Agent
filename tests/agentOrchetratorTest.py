import pytest
from unittest.mock import patch
from src.agentOrchestrator import run_agent

def test_agent_orchestrator():
    url = input("Enter the URL of the article you want to extract content from: ").strip()

    # Mock the content extraction, summarization, and search functions
    with patch("src.agent_orchestrator.extract_content_from_url") as mock_extract, \
         patch("src.agent_orchestrator.summarize_text") as mock_summarize, \
         patch("src.agent_orchestrator.search_related_content") as mock_search:

        # Define mock return values
        mock_extract.return_value = "This is the extracted content."
        mock_summarize.return_value = "This is summarized."
        mock_search.return_value = [
            {"title": "Related Article 1", "link": "https://link1.com"},
            {"title": "Related Article 2", "link": "https://link2.com"},
            {"title": "Related Article 3", "link": "https://link3.com"}
        ]

        # Run the agent orchestration
        result = run_agent(url)

        # Assert the mock results for each part of the pipeline
        mock_extract.assert_called_once_with(url)
        mock_summarize.assert_called_once_with("This is the extracted content.")
        mock_search.assert_called_once_with("This is summarized.")

        # Validate the final result (the output of the LangChain agent)
        assert "Related Article 1" in result
        assert "https://link1.com" in result
        assert "This is summarized." in result

        # Ensure the result contains all 3 search results
        assert "Related Article 2" in result
        assert "Related Article 3" in result

