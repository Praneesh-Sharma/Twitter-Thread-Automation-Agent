import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from googleSheetUpdate import update_google_sheet

# Test Data
topic = "AI advancements in gaming"
original_url = "https://blogs.nvidia.com/blog/ai-policy/"
twitter_thread_url = "https://twitter.com/example/status/1234567890"

# Call the update function
update_google_sheet(topic, original_url, twitter_thread_url)