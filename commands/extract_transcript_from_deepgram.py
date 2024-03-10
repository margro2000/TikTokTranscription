import asyncclick as click

import os

import sys
BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(BASE_DIR)

from Transcribe import extract_transcript_from_deepgram

@click.command()
@click.argument('filename')
async def extract_transcript(filename):
    """Simple program that greets NAME."""
    print(os.getcwd())
    path = os.path.join(BASE_DIR, 'public', filename)
    result = extract_transcript_from_deepgram(path)
    
    print(result)

if __name__ == '__main__':
    extract_transcript(_anyio_backend="asyncio")
