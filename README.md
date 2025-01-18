# Agent-Based-Twitter-Thread-Automation
This project automates content extraction, summarization, Twitter thread creation, and Google Sheets logging.

## Features
- Extract content from URLs.
- Summarize content with LLMs.
- Generate and post Twitter threads.
- Log details in Google Sheets.

## Getting Started

### **Prerequisites**
- Python 3.7+
- API keys for:
  - Groq API (for using the Groq model)
  - Twitter API (for posting tweets)
  - SerpAPI (for searching related content)
  - Google Sheets API (for updating the Google Sheets)

### Setup
1. Clone the repository:
    ```
    git clone https://github.com/Praneesh-Sharma/Agent-Based-Twitter-Thread-Automation.git
    cd multi-agent-system
    ```
2. Run the setup script
    ```
    bash setup.sh
    ```
3. Fill in your API keys in config/config.json
   - Create a config/config.json file in the root directory
   - Add your API keys for Groq, Twitter, SerpAPI, and Google Sheets in this file. Here's an example:
    ```
    {
        "groq_api_key": "your-groq-api-key",
        "twitter_api_key": "your-twitter-api-key",
        "twitter_api_secret_key": "twitter-api-secret-key",
        "twitter_access_token": "twitter-access-token",
        "twitter_access_token_secret": "twitter-access-token-secret",
        "serpapi_key": "your-serpapi-key",
        "google_sheets_api_key": "your-google-sheets-api-key"
    }
    ```

 4. Setup Google Cloud Services
   - Enable Required APIs
      - Go to the Google Cloud Console.
      - Select your project or create a new one.
      - Navigate to APIs & Services > Library.
      - Enable the following APIs: Google Drive API, Google Sheets API

### Usage
1. Activate the virtual environment
    ```
    source venv/bin/activate
    ```
2. Run the main script if you want to use the non-agent approach
    ```
    python main.py
    ```

3. Run this script if you want to use the agent approach
    ```
    python run.py
    ```

## **Explanation of Each Component**

1. **`run.py`**:
   - This is the main entry point for the automation process. It coordinates the steps involved in content extraction, summarization, web search for related content, Twitter post generation, posting the tweet, and updating the Google Sheet.
   - When executed, this script processes a provided URL and uses an agent to handle multiple tasks automatically, such as extracting content, generating a Twitter post, and posting it on Twitter. After posting, it updates a Google Sheet with the details of the post.

2. **`main.py`**:
   - This script performs the same high-level tasks as `run.py` but does not use the agent-based approach. Instead, it handles each step of the process sequentially.
   - The main steps are:
     1. **Extract Content**: Using the `extract_content_from_url()` function, it fetches the content from the provided URL.
     2. **Summarize Content**: It then summarizes the extracted content using the `summarize_text()` function.
     3. **Search Related Content**: The script uses the `search_related_content()` function to find relevant articles or content.
     4. **Generate Twitter Post**: It creates a concise tweet using the summarized content and `generate_twitter_post()`.
     5. **Post on Twitter**: It posts the generated tweet using the `ask_to_post()` function.
     6. **Update Google Sheets**: Finally, it updates the Google Sheet with the details of the posted tweet using `update_google_sheet()`.
   - Unlike `run.py`, this script doesn’t utilize an agent to manage these tasks and instead explicitly calls each function one after another.

3. **`contentExtraction.py`**:
   - This file contains the function `extract_content_from_url(url: str)` which is responsible for extracting content from a given URL.
   - The content can include text, articles, or other key information needed for summarization and related content searches. It handles the actual fetching of the webpage data, parsing it, and extracting usable text.

4. **`summarize.py`**:
   - The `summarize_text(content: str)` function is responsible for summarizing the extracted content from the URL.
   - This helps reduce long articles or complex content into concise summaries that are more suitable for generating short and engaging social media posts, like Twitter.

5. **`webSearch.py`**:
   - Contains the function `search_related_content(query: str)` that searches the web for related articles, news, or other content based on a given query.
   - It helps the system gather additional information relevant to the primary content, which can be used for enhancing the Twitter post and ensuring it’s backed by current or relevant information.

6. **`generateTwitterPost.py`**:
   - This component contains the function `generate_twitter_post(content: str, api_key: str)` that takes the summarized content and generates a concise Twitter post.
   - It is the core component for creating the Twitter content, ensuring that the final output is under Twitter's character limits and aligned with the required format.

7. **`postOnTwitter.py`**:
   - The `ask_to_post(twitter_post: str)` function in this file is responsible for posting the generated tweet to Twitter using the Twitter API.
   - It handles the interaction with Twitter's API to authenticate and submit the tweet, returning the URL of the posted tweet.

8. **`googleSheetUpdate.py`**:
   - This file contains the function `update_google_sheet(twitter_post, url, tweet_url)` which is responsible for updating a Google Sheet with the details of the posted tweet.
   - The Google Sheet serves as a log or record of all posts, including the tweet content, the URL from which the content was extracted, and the URL of the tweet on Twitter.

9. **`config/config.json`**:
   - This JSON configuration file stores API keys and other essential settings, such as the Groq API key for generating content using the language model.
   - The file makes it easy to manage and securely store configuration settings for your application without hardcoding sensitive information directly into the scripts.
