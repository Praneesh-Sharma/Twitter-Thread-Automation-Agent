import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from contentExtraction import extract_content_from_url # type: ignore

def main():
    # Accept URL input from the user
    url = input("Enter the URL of the article you want to extract content from: ").strip()
    
    # Extract content from the provided URL
    content = extract_content_from_url(url)
    
    if content:
        print("\nExtracted Content:\n")
        print(content[:1000])  # Display the first 1000 characters of the extracted content
    else:
        print("Failed to extract content. Please check the URL and try again.")

if __name__ == "__main__":
    main()
