import requests
import os
import json

from Search import search


def generate_url_profile(username: str) -> str:
    baseUrl = "https://www.tiktok.com/"
    if username.includes("@"):
        baseUrl = f"{baseUrl}{username}"
    else:
        baseUrl = f"{baseUrl}@{username}"
    return baseUrl


# def getIdVideo (url):
#     if(url.includes('/t/')):
#         # url = await new Promise((resolve) => {
#         #     require('follow-redirects').https.get(url, function(res) {
#         #         return resolve(res.responseUrl)
#         #     });
#         # })
#         url_request = requests.get(url, allow_redirects=True)
#         url = url_request.json()['url']
#     matching = url.includes("/video/")
#     if(not matching):
#         print("[X] Error: URL not found")
#         exit();

#     # Tiktok ID is usually 19 characters long and sits after /video/
#     idVideo = url.substring(url.indexOf("/video/") + 7, url.indexOf("/video/") + 26);
#     return (idVideo.length > 19) ? idVideo.substring(0, idVideo.indexOf("?")) : idVideo;


def getVideo(video_id, headers):
    print(f"DOWNLOAD VIDEO ID {video_id}")
    API_URL = f"https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id=${video_id}"
    request = requests.get(API_URL, headers=headers)
    body = request.text
    res = json.loads(body)

    # print(json.dumps(res, indent=2))

    # print("aweme list")
    # print(json.dumps(res["aweme_list"][0], indent=2))

    # print(res["aweme_list"][0]["aweme_id"])
    # print(video_id)
    # check if video was deleted
    # if res["aweme_list"][0]["aweme_id"] != video_id:
    #     print("RETURNING NONE")
    #     return None

    urlMedia = ""

    image_urls = []
    # check if video is slideshow
    if not (not "image_post_info" in res["aweme_list"][0]):
        print("[*] Video is slideshow")

        # get all image urls
        for element in res["aweme_list"][0]["image_post_info"]["images"]:
            # url_list[0] contains a webp
            # url_list[1] contains a jpeg
            image_urls.append(element["display_image"]["url_list"][1])

    else:
        # download_addr vs play_addr
        print(json.dumps(res["aweme_list"][0]["video"], indent=2))
        urlMedia = res["aweme_list"][0]["video"]["download_addr"]["url_list"][0]

    data = {"url": urlMedia, "images": image_urls, "id": video_id}

    return data


def download_media(item):
    root_dir = os.path.join(os.getcwd(), "downloads")
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)

    # print(item)

    # Slideshow
    if len(item["images"]) != 0:
        print("[*] Downloading Sildeshow")

        index = 0
        for image_url in item["images"]:
            fileName = f'{item["id"]}_{index}.jpeg'
            # check if file was already downloaded
            if os.path.exists(f"{root_dir}/{fileName}"):
                print(f'[!] File "{fileName}" already exists. Skipping')
                return
            index += 1

            downloadFile = requests.get(image_url)
            with open(f"{root_dir}/{fileName}", "wb") as file:
                file.write(downloadFile.content)

            downloadFile.close()
        return
    else:
        fileName = f'{item["id"]}.mp4'

        # check if file was already downloaded
        if os.path.exists(f"{root_dir}/{fileName}"):
            print(f'[!] File "{fileName}" already exists. Skipping')
            return

        # print(item)
        downloadFile = requests.get(item["url"])

        with open(f"{root_dir}/{fileName}", "wb") as file:
            file.write(downloadFile.content)


def download(id: str):
    headers = {
        "User-Agent": "TikTok 26.2.0 rv:262018 (iPhone; iOS 14.4.2; en_US) Cronet"
    }

    data = getVideo(id, headers)

    print("data")
    print(data)

    download_media(data)


tiktok = search("how to learn c++")


def download_video(url: str):
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "cookie": "ttwid=1%7CDsDzk1RUFUV4i6y1rJzuwU9w0xIxc4f8fO0fhbsw9nc%7C1707278561%7C942e27c48832e123e348144b45b8750a779548ec0ba1f0e5e9cacaa9ba7b01a7; tt_chain_token=ApH6wtAOE5eF0oXSWuyciQ==; tiktok_webapp_theme=light; passport_csrf_token=c470079011bf8b3849f11557dd4a8fe8; passport_csrf_token_default=c470079011bf8b3849f11557dd4a8fe8; _ttp=2dAOmdHyu6TJSNYgq3T91YcVY3C; tt_csrf_token=vZ8o9c9k-54ne7-_EfXkBqIZDwNhaTw-spnw; s_v_web_id=verify_ltkn9zky_HuUyt9Ca_Q9rT_4BHU_9tSM_mhRRLnK7Qbct; ak_bmsc=00F01881C96DEE65931DCC1CA22DC45E~000000000000000000000000000000~YAAQaCw+FwluUBaOAQAA24K6JRdmHQmxFg7uYLVL8dqfoflkMB5pHVTVFQmwHTVDpFT6eWvWFuQgdPhONXUZH3BOBNYJucga3lF8z0L1RfZ9mJatDaC0t6+rMkgRv9dBuykyBfLxb5Osz12G66saUxx+3ZhLu4W3669yGvMYxp/c1HfhhEp4R2NhNXGeX+vXA3TwwCm+IAA1IBFj7ho1BXMhqc+7WjaHh6mQ1QowWOZxbqRVYCdoY3SdME1zflpaV2C5a89w5zgYMsfcSatNdAhhoIhlRGbglsXy7+HeuCGAamNQO4IsWpeYRvBzLXCmZIMfDG4axY8CGvsWxKkqgWjaDxuDEudPdiixe+viLTh32SaV/0FEEB500bpS3PkT86CX0S77RxY=; multi_sids=7239075050450617387%3Aba3b5e524ba7189b4459810eab1b707c; cmpl_token=AgQQAPNSF-RO0rRIssD8sl0S_6KZhC6eP53ZYNF64w; sid_guard=ba3b5e524ba7189b4459810eab1b707c%7C1710030225%7C15551999%7CFri%2C+06-Sep-2024+00%3A23%3A44+GMT; uid_tt=87957f5d05f93fb909e3597ba08c0b434388539813a1d31ee7e7eeec37094f1f; uid_tt_ss=87957f5d05f93fb909e3597ba08c0b434388539813a1d31ee7e7eeec37094f1f; sid_tt=ba3b5e524ba7189b4459810eab1b707c; sessionid=ba3b5e524ba7189b4459810eab1b707c; sessionid_ss=ba3b5e524ba7189b4459810eab1b707c; sid_ucp_v1=1.0.0-KGI3OWM1MmYyYTAxYmU0YzYzZDAwMzUwYzE1MjJjYjcwZDEzYjQwYjEKIAiriIKk94yXu2QQkfuzrwYYswsgDDDpudmjBjgEQOoHEAQaB3VzZWFzdDUiIGJhM2I1ZTUyNGJhNzE4OWI0NDU5ODEwZWFiMWI3MDdj; ssid_ucp_v1=1.0.0-KGI3OWM1MmYyYTAxYmU0YzYzZDAwMzUwYzE1MjJjYjcwZDEzYjQwYjEKIAiriIKk94yXu2QQkfuzrwYYswsgDDDpudmjBjgEQOoHEAQaB3VzZWFzdDUiIGJhM2I1ZTUyNGJhNzE4OWI0NDU5ODEwZWFiMWI3MDdj; store-idc=useast5; store-country-code=us; store-country-code-src=uid; tt-target-idc=useast5; tt-target-idc-sign=ieIXMhh_0EMY78JudBHjG-7l2x5L3QYp3-3_jWexxGfD92Rmd6qXsfQB6iqy0aegLRSmU58MjFeSlpQwVcxOmIVboow0OJn_oqzSCqfowTxoGDErFW_0qSasmhST259LR1-C0UnYc_u1MyIidx_KXTgb1JjZcvF35cDgZSq8NL_DzATK5JC6sE9KNn3oCGD5ywxLVLwje5gKdKwRudMEIVsCZkdbwEsPjBtWocOCMi9Q7Ii2E0iGQVA74rwAcKsn1PbuaXeK8x0yygrsydnF0Tgmy0iD2o_o5E7ciO_piFHI86imPytX1wtg2ug86q_S_-aWnp_YQWg1Y-c5SZtUwxYWAQAVCqx30gQFKkn0MF414t97nEgbCLIoqHOC_GewnwxRYN--MuXGsmrsAH7gqtx2BlhWrzlbOpoBhKlWtxR972htSGT02lw9v29fxWuTYsiRpG_lLoo69FaqmyvQgZaqm7OJlduehw4zzsozx0_GSnx6HInTzcexUhD2CwE3; last_login_method=handle; perf_feed_cache={%22expireTimestamp%22:1710201600000%2C%22itemIds%22:[%227337387375468842272%22%2C%227328222764383423749%22%2C%227340435991565520170%22]}; msToken=G3f_9ZLeWq1ILPc7mEAZL5KrCAeLmtUbhIWIU5lH6tAGS3bqzZ6ZCOa_Ht4IExXHuPCLtP6FuaTeB5MNa4ySa9gAdURZmRRgG6tvp9M2BB5imiOdX1jNRZ6Se73J6w8UfLh4IBq_fE6XoJvu; msToken=JIk50O8QR3_BkPbiMQlOiu14nujJOk40Skwf0UuhbvyMZmLDGDlT5v0AuoD76bPUdN5rLmEetfjSZrNRtlg-dNXJnzMgSgpqMho0sLE4T85ouxre2mAtPTmG-bnbPS9uYh-YMPDyw00Xz0Lm; bm_sv=9E47556A70DD37AB94C93C201C0A6CD3~YAAQSSw+Fz1a3xeOAQAAVxbHJRdasecqSUMxYbXyPae16VZ4cSfIQTGQ/S7S7njWm42Xqj6ExQK64mYh3XzF+l/yepjtrjstvg1Zs8X55oHoYD0EyA3ILrZu/Zcs+w2ad+O9dFnukv07IBFD7Uvmuz/iBUg0Rgz/iBWHCSQ5/f8DB5i+LCGq9EfmPjHo9N5pmzyKqw5am73pU1KNoioOZcfnPjE4U+lv2uCSfBmKpTyFoh7bC3q+vOnMCJRLdyIM~1; passport_fe_beating_status=true; odin_tt=8de55a7699b0b567a03ffdbb9fa570638dc03046344e8c3a4096de7466b793ac6b5f652a237f2945a19792d81b683c9b0d78eb3e7e4cadbf20a2e202e86a9e5c006b476adbb24324be0fa3e1e94b81d0",
        "Referrer-Policy": "strict-origin-when-cross-origin",
    }

    with requests.session() as session:
        response = session.get(url, headers=headers)

        # print(response.content)


# print(tiktok)
download(tiktok)
