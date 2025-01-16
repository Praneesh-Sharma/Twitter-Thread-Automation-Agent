import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from contentExtraction import extract_content_from_url  # type: ignore
from summarize import summarize_text  # type: ignore
from webSearch import search_related_content  # type: ignore

def main():
    try:
        # Step 1: Ask the user for a URL
        url = input("Enter the URL to process: ")
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
            print("No results found.")
            return

        # Display the final results
        print("\nPipeline Complete!")
        print(f"\nSummarized Content: {summarized_content}")
        print("\nTop 3 search results:")
        for result in search_results:
            print(f"- {result['title']}: {result['link']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
