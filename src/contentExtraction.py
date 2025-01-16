from newspaper import Article
import logging

# Set up logging for better traceability
logging.basicConfig(level=logging.INFO)

def extract_content_from_url(url):
    """Extract main content from a news article URL."""
    try:
        article = Article(url)
        article.download()  # Download the article
        article.parse()  # Parse the article content
        logging.info(f"Successfully extracted content from {url}")
        return article.text  # Return the extracted content (text)
    except Exception as e:
        logging.error(f"Error extracting content from {url}: {e}")
        return None