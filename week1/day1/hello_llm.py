import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

# load .env file for api keys
load_dotenv()

# fetch api key
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found")

# register as client
client = Groq(api_key = my_api_key)

# choose a model
model = "openai/gpt-oss-120b"
role="user"
prompt = "Who is Virat Kohli?"

# create a message
message = {
    "role" : role,
    "content" : prompt
}

# we have to pass array of messages
messages = [message]

# make a API call and get the response
response = client.chat.completions.create(model = model, messages = messages)
# print(response)


print("############################################################")

answer = response.choices[0].message.content
print(answer)
