import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from contentExtraction import extract_content_from_url #type: ignore
from summarize import summarize_text # type: ignore

# Function to extract and summarize content from URL
def extract_and_summarize(url):
    # Extract content from the URL
    content = extract_content_from_url(url)
    
    if content:
        print("Original Content Extracted:")
        print(content)
        print("\nSummarized Content:")
        # Summarize the content
        summary = summarize_text(content)
        print(summary)
    else:
        print("No content extracted.")

if __name__ == "__main__":
    # Accept the URL from the user
    url = input("Enter the URL to summarize: ")
    extract_and_summarize(url)
