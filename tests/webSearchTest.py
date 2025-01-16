import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from webSearch import search_related_content # type: ignore

# Test the function with a sample query
if __name__ == "__main__":
    query = input("Enter search query: ")
    results = search_related_content(query)

    if results:
        print("\nTop 3 search results:")
        for result in results:
            print(f"Title: {result['title']}")
            print(f"Link: {result['link']}")
            print()
    else:
        print("No results found.")
