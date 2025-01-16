import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from contentExtraction import extract_content_from_url  # type: ignore
from summarize import summarize_text  # type: ignore
from webSearch import search_related_content  # type: ignore

# Test the function with a sample query
if __name__ == "__main__":
    url = input("Enter the URL to process: ")

    print("Extracting content from the URL...")
    extracted_content = extract_content_from_url(url)
    if not extracted_content:
        print("Failed to extract content. Please try with a different URL.")
    
    print(f"\nExtracted Content:\n{extracted_content[:500]}...")

    print("\nSummarizing the content...")
    summarized_content = summarize_text(extracted_content)
    if not summarized_content:
        print("Failed to summarize the content. Please try again.")
    
    print(f"\nSummarized Content: {summarized_content}")

    print("\nSearching for related content on the web...")
    search_results = search_related_content(summarized_content)
    if not search_results:
        print("No results found.")

    print("\nTop 3 search results:")
    for result in search_results:
        print(f"Title: {result['title']}")
        print(f"Link: {result['link']}")
        print()   
