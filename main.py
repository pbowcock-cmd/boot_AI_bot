import os
from dotenv import load_dotenv
import argparse
from prompts import system_prompt
from call_function import available_functions
from call_function import call_function
import json
import sys

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
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()



# Now we can access `args.user_prompt`
content=args.user_prompt

messages = [{"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]
for n in range(20):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
)

    if args.verbose==True:
        print (f"User prompt: {args.user_prompt}")
        print (f"Prompt tokens: {response.usage.prompt_tokens}")
        print (f"Response tokens: {response.usage.completion_tokens}")

    if response.usage == None:
        raise RuntimeError
        #print(f'Prompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}')
    #
    message = response.choices[0].message
    messages.append(message)
    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message=call_function(tool_call,args.verbose)
            if not result_message.get("content"):
                raise RuntimeError(f"Empty function response for {tool_call.function.name}")
            if args.verbose:
                 print(f"-> {result_message['content']}")
                #function_args = json.loads(tool_call.function.arguments or "{}")
                # print(f"Calling function: {tool_call.function.name}({function_args})")
            messages.append(result_message)
    else:
        print (f"{message.content}")
        break
else:
        print("agent hit the maximum number of iterations without a final response")
        sys.exit(1)
