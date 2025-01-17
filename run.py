import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from agentOrchestrator import run_agent

def main():
    # Prompt the user to input the URL
    url = input("Please enter the URL to process: ").strip()

    if not url:
        print("URL cannot be empty. Please provide a valid URL.")
        return

    print(f"Starting agent to process URL: {url}")
    try:
        # Call the run_agent function
        result, twitter_post, twitter_url = run_agent(url)
        
        print("\nAgent Processing Completed!")
        print(f"Result: {result}")
        print(f"Twitter Post: {twitter_post}")
        print(f"Twitter URL: {twitter_url}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
