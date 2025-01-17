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
    model_max_tokens = 1000       # Max tokens the summarizer can handle
    twitter_post_max_tokens = 150  
    
    # Helper function: Split text into chunks
    def split_into_chunks(text, max_length):
        # Split the text into words and keep track of token count
        words = text.split()
        chunks = []
        current_chunk = []
        current_token_count = 0
        
        for word in words:
            # Approximate token count per word
            word_token_count = len(word.split())
            if current_token_count + word_token_count <= max_length:
                current_chunk.append(word)
                current_token_count += word_token_count
            else:
                chunks.append(' '.join(current_chunk))
                current_chunk = [word]
                current_token_count = word_token_count
        
        # Add the last chunk if any
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        return chunks
    
    # Helper function: Log token counts
    def log_token_info(text, stage):
        token_count = len(text.split())
        print(f"[INFO] {stage}: Token count = {token_count}")
    
    # Log the initial input size
    log_token_info(input_text, "Initial Input")
    
    # Step 1: Break large input into manageable chunks
    if len(input_text.split()) > model_max_tokens:
        print("[INFO] Input text exceeds model token limit. Splitting into chunks...")
        chunks = split_into_chunks(input_text, model_max_tokens)
    else:
        chunks = [input_text]
    
    # Step 2: Summarize each chunk using the custom summarizer
    summarized_chunks = []
    for idx, chunk in enumerate(chunks):
        log_token_info(chunk, f"Chunk {idx + 1}")
        print(f"[INFO] Summarizing Chunk {idx + 1} using custom summarizer...")
        try:
            # Limit each chunk to 150 tokens for the summarizer (adjust as needed)
            chunk_summary = summarize_text(chunk, max_length=150)
            summarized_chunks.append(chunk_summary)
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
                "content": f"Create a Twitter post of approximately 200 to 250 characters based on this: {combined_summary} ",
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
