from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_openai_response(prompt, system_prompt="You are a helpful master tutor AI living in the backend of a consumer app. Teach in very small atomic bite-sized chunks.", model="gpt-4", response_format="text"):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]
    if response_format == "json":
        response = client.chat.completions.create(
            model=model,
            messages=messages, response_format={"type": "json_object"})
    else:
        response = client.chat.completions.create(
            model=model,
            messages=messages)

    assistant_reply = response.choices[0].message.content

    return assistant_reply
