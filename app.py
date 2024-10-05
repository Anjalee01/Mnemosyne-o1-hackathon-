import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
user_content = input("User: ")

api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(
    api_key=api_key,
    base_url="https://api.aimlapi.com/",
)

chat_completion = client.chat.completions.create(
    model="o1-mini",
    messages=[
        {"role": "user", "content": user_content},
    ],
    max_tokens=2000,
)

response = chat_completion.choices[0].message.content
print("Response:\n", response)
