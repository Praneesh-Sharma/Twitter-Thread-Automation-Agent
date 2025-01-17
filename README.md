# Agent-Based-Twitter-Thread-Automation
This project automates content extraction, summarization, Twitter thread creation, and Google Sheets logging.

## Features
- Extract content from URLs.
- Summarize content with LLMs.
- Generate and post Twitter threads.
- Log details in Google Sheets.

## Getting Started

### Prerequisites
- Python 3.7+
- API keys for OpenAI, Twitter, SerpAPI, and Google Sheets.

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