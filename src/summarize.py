from transformers import pipeline

# Load pre-trained model for summarization
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def split_text_into_chunks(text, max_tokens=1024):
    """
    Splits the input text into smaller chunks based on the max token limit.

    Parameters:
        text (str): The input text to split.
        max_tokens (int): The maximum number of tokens per chunk.

    Returns:
        list: A list of text chunks.
    """
    words = text.split()
    chunks = [" ".join(words[i:i + max_tokens]) for i in range(0, len(words), max_tokens)]
    return chunks

def summarize_text(text, max_length=50, min_length=25,verbose=False):
    """
    Summarizes long text by splitting it into smaller chunks.

    Parameters:
        text (str): The input text to summarize.
        max_length (int): The maximum length of the summary in tokens.
        min_length (int): The minimum length of the summary in tokens.

    Returns:
        str: The combined summary of all chunks.
    """
    try:
        # Split the text into chunks
        chunks = split_text_into_chunks(text)
        summaries = []

        for i, chunk in enumerate(chunks):
            if verbose:  # Only print details if verbose is True
                print(f"[INFO] Summarizing Chunk {i+1}/{len(chunks)}: Token count = {len(chunk.split())}")
            
            try:
                # Summarize each chunk
                summary = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
                summaries.append(summary[0]['summary_text'])
            except Exception as e:
                if verbose:  # Log errors only if verbose is True
                    print(f"[ERROR] Failed to summarize Chunk {i+1}: {e}")

        return " ".join(summaries)  # Combine the summaries of all chunks
    except Exception as e:
        if verbose:  # Log errors only if verbose is True
            print(f"[ERROR] Failed to summarize text: {e}")
        return None

