import anthropic
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def get_message_from_anthropic(prompt):
    text = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=2000,
        system="You are a helpful master tutor AI living in the backend of a consumer app. Teach in very small atomic bite-sized chunks",
        messages=[
            {"role": "user", "content": prompt}
        ]
    ).content[0].text
    
    return text
