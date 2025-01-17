import requests
import json
from requests_oauthlib import OAuth1Session

# Load Twitter credentials from config
def load_twitter_credentials():
    """Load Twitter API credentials from config.json"""
    try:
        with open('config/config.json', 'r') as f:
            config = json.load(f)
            return {
                "api_key": config.get('twitter_api_key'),
                "api_secret_key": config.get('twitter_api_secret_key'),
                "access_token": config.get('twitter_access_token'),
                "access_token_secret": config.get('twitter_access_token_secret')
            }
    except FileNotFoundError:
        print("Config file not found.")
        return None
    except json.JSONDecodeError:
        print("Error reading the config file.")
        return None

# Function to post a tweet on Twitter using OAuth 1.0a (User Context)
def post_on_twitter(tweet_text: str):
    """Post a tweet on Twitter using OAuth 1.0a User Context."""
    try:
        credentials = load_twitter_credentials()
        if not credentials:
            print("Twitter credentials missing or incorrect.")
            return

        # Set up OAuth1 session
        oauth = OAuth1Session(
            client_key=credentials["api_key"],
            client_secret=credentials["api_secret_key"],
            resource_owner_key=credentials["access_token"],
            resource_owner_secret=credentials["access_token_secret"]
        )

        # Construct the API URL for posting a tweet using v2 endpoint
        url = "https://api.twitter.com/2/tweets"

        # Construct the payload for the tweet
        payload = {
            "text": tweet_text  # For API v2, use "text" instead of "status"
        }

        # Send the POST request to create the tweet
        response = oauth.post(url, json=payload)

        # Handle the response
        if response.status_code == 201:
            print("Tweet posted successfully!")
        else:
            print(f"Error posting tweet: {response.status_code}, {response.text}")

    except Exception as e:
        print(f"Error posting tweet: {e}")

# Function to ask user if they want to post the tweet or cancel
def ask_to_post(tweet_text: str):
    """Ask the user if they want to post the tweet or cancel."""
    # print("\nGenerated Twitter Post:")
    # print(tweet_text)

    user_input = input("\nDo you want to post this tweet? (yes/no): ").strip().lower()

    if user_input == "yes":
        post_on_twitter(tweet_text)
    else:
        print("Tweeting has been canceled.")
