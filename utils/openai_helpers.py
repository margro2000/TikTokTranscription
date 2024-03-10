from urllib.parse import urlparse, unquote
import requests
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


def download_image(openai_image_url):
    # Parse the URL to extract the path, then unquote to decode percent-encoded characters
    parsed_url = urlparse(openai_image_url)
    path = unquote(parsed_url.path)

    # Extract the filename from the URL path
    filename = os.path.basename(path)

    # Specify the directory where you want to save the image
    root_dir = os.path.join(os.getcwd(), "downloads")
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    # Full path for the file
    file_path = os.path.join(root_dir, filename)

    # Check if the file already exists
    if os.path.exists(file_path):
        print(f"File '{filename}' already exists. Skipping download.")
        return file_path

    # Download the image
    response = requests.get(openai_image_url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"File '{filename}' downloaded successfully.")
        return file_path
    else:
        print(
            f"Failed to download the file. Status code: {response.status_code}")
        return None


def generate_openai_image(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    print(response)
    image_url = response.data[0].url
    return download_image(image_url)


if __name__ == "__main__":
    print("hello")
    print(generate_openai_image("learn html"))
