# This is a small LLM program 
from openai import OpenAI

client = OpenAI(
  # API Key from openai, DO NOT SHARE
  api_key=''
)

completion = client.chat.completions.create(
  model="gpt-4o-mini-2024-07-18",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message.content)
