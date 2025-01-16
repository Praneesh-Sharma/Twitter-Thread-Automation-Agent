from transformers import pipeline

# Load pre-trained model for summarization
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# Function to summarize content to 4-8 words
def summarize_text(text):
    # Get summary (we limit the max_length to around 8 words, to ensure brevity)
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']
