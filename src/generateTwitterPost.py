from groq import Groq

def generate_twitter_post(input_text, api_key):
    # Initialize the Groq client with your API key
    client = Groq(api_key=api_key)

    # Create the chat completion request
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "system",
            "content": "You are a Twitter post generator that writes concise and engaging posts."
        }, {
            "role": "user",
            "content": f"Create a Twitter post of approximately 75 to 100 words based on this: {input_text}",
        }],
        model="llama-3.3-70b-versatile",
        temperature=0.8,  # Adjust temperature for creativity in post
        max_tokens=150,  # Limit to Twitter's character limit
        top_p=1,
        stop=None,
        stream=False,
    )

    # Return the generated Twitter post
    return chat_completion.choices[0].message.content.strip()
