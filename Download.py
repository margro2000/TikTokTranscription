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

    filename = f'{item["id"]}.mp4'

    path = f"{root_dir}/{filename}"

    # check if file was already downloaded
    if os.path.exists(path):
        print(f'[!] File "{filename}" already exists. Skipping')
    else:
        downloadFile = requests.get(item["url"])

        with open(path, "wb") as file:
            file.write(downloadFile.content)

    return {
        "path": path,
        "filename": filename
    }


def download_video_from_tiktok(query, index=0):
    headers = {
        "User-Agent": "TikTok 26.2.0 rv:262018 (iPhone; iOS 14.4.2; en_US) Cronet"
    }

    id = search(query, index)

    data = getVideo(id, headers)

    return download_media(data)


@click.command()
@click.argument("query")
def download(query):
    return download_video_from_tiktok(query)


if __name__ == "__main__":
    download()
