import sys
import os
import re

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from contentExtraction import extract_content_from_url  # type: ignore
from summarize import summarize_text  # type: ignore
from webSearch import search_related_content  # type: ignore


def is_valid_url(url: str) -> bool:
    """Validate if the provided URL is in the correct format."""
    regex = r'^(https?://)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}(/.*)?$'
    return re.match(regex, url) is not None


def main():
    try:
        # Step 1: Ask the user for a URL
        url = input("Enter the URL to process: ").strip()

        if not url:
            print("URL cannot be empty. Please provide a valid URL.")
            return

        # Validate the URL format
        if not is_valid_url(url):
            print("Invalid URL format. Please enter a valid URL.")
            return

        print("\nProcessing the URL...")

        # Step 2: Extract content from the URL
        extracted_content = extract_content_from_url(url)
        if not extracted_content:
            print("Failed to extract content. Please try with a different URL.")
            return

        # Step 3: Summarize the extracted content
        summarized_content = summarize_text(extracted_content)
        if not summarized_content:
            print("Failed to summarize the content. Please try again.")
            return

        # Step 4: Search the summarized content on the web
        search_results = search_related_content(summarized_content)
        if not search_results:
            print("No related search results found.")
            return

        # Step 5: Extract content from the search results' links
        combined_extracted_content = ""
        for result in search_results[:3]:  # Limiting to top 3 results
            link = result.get('link')
            if link:
                print(f"\nExtracting content from: {link}")
                additional_content = extract_content_from_url(link)
                if additional_content:
                    combined_extracted_content += f"\n\n--- Extracted from {link} ---\n"
                    combined_extracted_content += additional_content
                else:
                    print(f"Failed to extract content from {link}")

        if not combined_extracted_content:
            print("No additional content could be extracted from the search results.")
            return

        # Display the final combined results
        print("\nPipeline Complete!")
        print(f"\nSummarized Content: {summarized_content}")
        print(f"\nCombined Extracted Content from Top 3 Search Results: {combined_extracted_content}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
