import openai
openai.api_key = 'your-api-key-here'

def generate_text(prompt, model="gpt-3.5-turbo", max_tokens=150, temperature=0.7):
    """
    Generate text using GPT-3.5 based on a given prompt.
    
    Args:
        prompt (str): The input prompt to GPT-3.
        model (str): The GPT-3 model to use. Options: "gpt-3.5-turbo", "gpt-4", etc.
        max_tokens (int): The maximum number of tokens in the generated text.
        temperature (float): Controls randomness in text generation. Range 0 to 1 (higher values mean more random output).
    
    Returns:
        str: The generated text response from GPT-3.
    """
    response = openai.ChatCompletion.create(
        model=model,  
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    
    return response['choices'][0]['message']['content'].strip()

prompt = "Write a short story about a time-traveling robot who saves humanity."
generated_text = generate_text(prompt)
print(generated_text)
