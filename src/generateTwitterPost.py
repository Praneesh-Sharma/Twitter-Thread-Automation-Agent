from groq import Groq
from summarize import summarize_text

def generate_twitter_post(input_text, api_key):
    """
    Generates a Twitter post based on the given input text using the Groq API.
    Summarizes content using a custom summarizer function.
    """
    # Initialize the Groq client with your API key
    client = Groq(api_key=api_key)
    
    # Define constraints
    model = "llama-3.3-70b-versatile"
    max_tokens_per_request = 6000  # Chunk splitting threshold
    model_max_tokens = 1024       # Max tokens the summarizer can handle
    twitter_post_max_tokens = 150  
    
    # Helper function: Split text into chunks
    def split_into_chunks(text, max_length):
        sentences = text.split('. ')
        chunks = []
        current_chunk = []
        current_length = 0
        
        for sentence in sentences:
            sentence_tokens = len(sentence.split())
            if current_length + sentence_tokens <= max_length:
                current_chunk.append(sentence)
                current_length += sentence_tokens
            else:
                chunks.append('. '.join(current_chunk))
                current_chunk = [sentence]
                current_length = sentence_tokens
        
        # Add the last chunk
        if current_chunk:
            chunks.append('. '.join(current_chunk))
        return chunks
    
    # Helper function: Log token counts
    def log_token_info(text, stage):
        token_count = len(text.split())
        print(f"[INFO] {stage}: Token count = {token_count}")
    
    # Log the initial input size
    log_token_info(input_text, "Initial Input")
    
    # Step 1: Break large input into manageable chunks
    if len(input_text.split()) > max_tokens_per_request:
        print("[INFO] Input text exceeds max tokens per request. Splitting into chunks...")
        chunks = split_into_chunks(input_text, model_max_tokens)
    else:
        chunks = [input_text]
    
    # Step 2: Summarize each chunk using the custom summarizer
    summarized_chunks = []
    for idx, chunk in enumerate(chunks):
        log_token_info(chunk, f"Chunk {idx + 1}")
        print(f"[INFO] Summarizing Chunk {idx + 1} using custom summarizer...")
        try:
            summary = summarize_text(chunk, max_length=150)
            summarized_chunks.append(summary)
        except Exception as e:
            print(f"[ERROR] Failed to summarize Chunk {idx + 1}: {e}")
    
    # Combine all summaries
    combined_summary = " ".join(summarized_chunks)
    log_token_info(combined_summary, "Combined Summary")
    
    # Step 3: Generate the Twitter post from the summarized content
    print("[INFO] Generating Twitter post...")
    try:
        chat_completion = client.chat.completions.create(
            messages=[{
                "role": "system",
                "content": "You are a Twitter post generator that writes concise and engaging posts."
            }, {
                "role": "user",
                "content": f"Create a Twitter post of approximately 75 to 100 words based on this: {combined_summary}",
            }],
            model=model,
            temperature=0.8,  # Adjust temperature for creativity
            max_tokens=twitter_post_max_tokens,
            top_p=1,
            stop=None,
            stream=False,
        )
        twitter_post = chat_completion.choices[0].message.content.strip()
        print("[INFO] Twitter post generated successfully.")
        return twitter_post
    except Exception as e:
        print(f"[ERROR] Failed to generate Twitter post: {e}")
        return None