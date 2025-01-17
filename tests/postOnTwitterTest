import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from postOnTwitter import post_on_twitter, ask_to_post

def test_post_on_twitter():
    """Test the Twitter post functionality."""
    tweet_text = "This is a test tweet from the automation script."
    print("\nTesting Twitter post...")
    tweet_url = post_on_twitter(tweet_text)  # This will attempt to post the tweet and return the URL
    
    if tweet_url:
        print(f"Tweet URL: {tweet_url}")
    else:
        print("Failed to post tweet.")

def test_ask_to_post():
    """Test the prompt for posting the tweet and return the tweet URL."""
    tweet_text = "This is another test tweet. Do you want to post this?"
    print("\nTesting post or cancel prompt...")
    tweet_url = ask_to_post(tweet_text)  # This will ask the user to confirm the post or cancel
    return tweet_url  # Return the tweet URL

if __name__ == "__main__":
    # Run tests
    # Uncomment the test you want to run
    # test_post_on_twitter()
    tweet_url = test_ask_to_post()
    
    if tweet_url:
        print(f"Tweet posted successfully! URL: {tweet_url}")
    else:
        print("Tweet was not posted.")
