import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

system_content = (
    "You are a helpful computer science professor"
    # "You are a dimensional data modeling assistant."
    # "You specialize in Kimball Data Warehousing methodologies."
    # "You also consider modern data modeling best practices, even if they conflict with Kimball."
    # "You always try to give the best advice possible and explain the tradeoffs of each approach."
    # "You provide answers in well formatted markdown, using mermaid diagrams and tables to illustrate points as much as possible."
)

user_content = (
    "Teach me about Makefiles."
)

completion = openai.ChatCompletion.create(
    # model="gpt-3.5-turbo",
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content}
    ],
    temperature=0.2, # between 0 (deterministic) and 1 (random)
    stream=True
)

output = open("gpt_output.md", "w")
output.write("> # " + user_content + "\n\n")
output.close()

for chunk in completion:
    content = chunk.choices[0].get("delta", {}).get("content")
    output = open("gpt_output.md", "a")
    if content is not None:
        output.write(content)
    output.close()
