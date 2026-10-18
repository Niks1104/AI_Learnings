import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

client = Groq(api_key = my_api_key)

model = "openai/gpt-oss-120b"

role = "user"
prompt1 = "Hi!"
prompt2 = "Explain time travel in detail under 100 words"
prompt3 = "Write a 1000 word essay on Machine Learning"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {
        "role": role,
        "content" : prompt
    }

    messages = [message]

    # we can limit token usage by using max_tokens
    response = client.chat.completions.create(model = model, messages = messages, max_tokens= 5000)
    usage = response.usage

    # finish_reason defines, it stops naturally or usgae of token
    print(f"Prompt : {prompt} -- Input Token {usage.prompt_tokens} Completion Token {usage.completion_tokens} Total Tokens {usage.total_tokens} Finish reason : {response.choices[0].finish_reason}")