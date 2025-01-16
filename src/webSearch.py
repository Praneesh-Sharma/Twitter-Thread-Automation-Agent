from serpapi import GoogleSearch
import json

# Fetch the API key from the config file
def get_api_key():
    with open('config/config.json', 'r') as file:
        config_data = json.load(file)
        return config_data["serp_api_key"]

# Function to search for related content using SerpAPI
def search_related_content(query):
    # Get the API key from config
    api_key = get_api_key()

    # Parameters for the search
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # Check if there are results and return the first 3
    if 'organic_results' in results:
        return results['organic_results'][:3]  # Limit to the first 3 results
    else:
        print("No results found.")
        return []
