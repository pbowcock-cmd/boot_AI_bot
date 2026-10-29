import os
from dotenv import load_dotenv
import argparse

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key==None:
    raise RuntimeError ("Missing Key")

# AI links
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)
response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        }
    ],
)
if response.usage == None:
    raise RuntimeError
print(f'Prompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}')

print (f"{response.choices[0].message.content}")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()
# Now we can access `args.user_prompt`
content=args.user_prompt
