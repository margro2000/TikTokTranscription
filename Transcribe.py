import requests
from dotenv import load_dotenv
import os
from utils.openai_helpers import get_openai_response

# Load environment variables
load_dotenv()


def extract_transcript_from_deepgram(video_file_path):
    api_key = os.getenv('DEEPGRAM_API_KEY')
    url = 'https://api.deepgram.com/v1/listen?smart_format=true&language=en&model=nova-2'
    headers = {
        'Authorization': f'Token {api_key}',
        'Content-Type': 'audio/mp4'  # Adjust based on your file's actual type
    }
    with open(video_file_path, 'rb') as file:
        response = requests.post(url, headers=headers, data=file)
    response.raise_for_status()
    data = response.json()
    transcript = data['results']['channels'][0]['alternatives'][0]['transcript']
    return transcript


def is_transcript_usable(transcript: str) -> bool:
    prompt = f""""
    Is the following transcript usable? 
    i.e. can meaningful questions and answers be derived from it?
    
    Please answer with the single word "yes" or "no".

    Transcript:
    {transcript}
    
    Usable?
    """

    answer = get_openai_response(prompt)

    return "yes" in answer.lower()
