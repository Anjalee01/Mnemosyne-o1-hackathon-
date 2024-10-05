import os
from openai import OpenAI

user_content = """
how many Rs are there in the word strawberry
think step by step
"""

client = OpenAI(
    api_key="d2a52fb173584df59d1d3525d7ed39f1",
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