import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from generateTwitterPost import generate_twitter_post  # type: ignore

# Fetch the API key from the config file
with open('config/config.json', 'r') as file:
    config_data = json.load(file)
    api_key = config_data["groq_api_key"]
    print(api_key)

if __name__ == "__main__":
    input_text = input("Enter original text:\n")
    generated_post = generate_twitter_post(input_text, api_key)
    print(f"Generated Twitter Post: {generated_post}")
