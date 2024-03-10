from openai import OpenAI

API_KEY = "3YQiOZoqSS6qHJj6I2cVpq2mO0pZXxjQ"


def ask_solar(prompt, system_prompt="You are a helpful master tutor AI living in the backend of a consumer app. Teach in very small atomic bite-sized chunks."):
    client = OpenAI(
        api_key=API_KEY,
        base_url="https://api.upstage.ai/v1/solar"
    )
    response = client.chat.completions.create(
        model="solar-1-mini-chat",
        messages=[
            {
              "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print(ask_solar("What is the weather like today?"))
