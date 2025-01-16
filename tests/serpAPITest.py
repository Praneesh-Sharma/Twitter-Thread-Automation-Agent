# test_serpapi.py
from serpapi import GoogleSearch
import json

# Fetch the API key from the config file
with open('config/config.json', 'r') as file:
    config_data = json.load(file)
    api_key = config_data["serp_api_key"]

print(api_key)

# Define the search query for "hidevs"
params = {
    "engine": "google", # Search engine
    "q": "hidevs",  # Search query
    "api_key": api_key  # Your SerpApi key from config
}

# Create a search instance
search = GoogleSearch(params)

# Get the search results in a dictionary format
results = search.get_dict()

# Print the titles and links of the top results
if 'organic_results' in results:
    top_results = results['organic_results'][:3]
    for result in top_results:
        print(f"Title: {result['title']}")
        print(f"Link: {result['link']}")
        print()
else:
    print("No results found or error occurred.")