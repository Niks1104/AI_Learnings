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
role="user"
prompt="Suggest a name for my food company in one word"

message_system ={
    "role" : "system",
    "content" : "You are a brand manager of my food company. Give me answer in one word"
}

message = {
    "role": role,
    "content": prompt
}

messages = [message_system, message]

# temperature definesLLM personality and it ranges between 0 to 2; 0 - safe, 2- creative
# by default it is 0
response = client.chat.completions.create(model=model, messages= messages, temperature = 2)
answer = response.choices[0].message.content
print(answer)