import requests
import os
import json
import asyncclick as click

from Search import search


def getVideo(video_id, headers):
    print(f"DOWNLOAD VIDEO ID {video_id}")
    API_URL = f"https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={video_id}"
    request = requests.get(API_URL, headers=headers)
    body = request.text
    res = json.loads(body)

    with open("response.json", "w") as file:
        file.write(json.dumps(res, indent=2))

    urlMedia = res["aweme_list"][0]["video"]["play_addr"]["url_list"][0]

    data = {"url": urlMedia, "id": video_id}

    return data


def download_media(item):
    root_dir = os.path.join(os.getcwd(), "downloads")
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)

    fileName = f'{item["id"]}.mp4'

    # check if file was already downloaded
    if os.path.exists(f"{root_dir}/{fileName}"):
        print(f'[!] File "{fileName}" already exists. Skipping')
        return

    downloadFile = requests.get(item["url"])

    with open(f"{root_dir}/{fileName}", "wb") as file:
        file.write(downloadFile.content)


@click.command()
@click.argument("query")
async def download(query):
    headers = {
        "User-Agent": "TikTok 26.2.0 rv:262018 (iPhone; iOS 14.4.2; en_US) Cronet"
    }

    id = search(query)

    data = getVideo(id, headers)

    download_media(data)


if __name__ == "__main__":
    download()
