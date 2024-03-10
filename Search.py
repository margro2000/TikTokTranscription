import requests
import urllib.parse
import json
import sys

# Make an API call and store the response.
# query = "how to learn c++"
# query = sys.argv[1] if len(sys.argv) > 1 else query


def search(query: str):
    query = urllib.parse.quote(query)

    url = f"https://www.tiktok.com/api/search/general/full/?WebIdLastTime=1707278561&aid=1988&app_language=en&app_name=tiktok_web&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=MacIntel&browser_version=5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2010_15_7%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F122.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_id=7332705406432642591&device_platform=web_pc&device_type=web_h264&focus_state=true&from_page=search&history_len=10&is_fullscreen=true&is_page_visible=true&keyword={query}&offset=0&os=mac&priority_region=US&referer=https%3A%2F%2Fwww.tiktok.com%2F&region=US&root_referer=https%3A%2F%2Fwww.tiktok.com%2F&screen_height=982&screen_width=1512&search_source=normal_search&tz_name=America%2FLos_Angeles&verifyFp=verify_ltkn9zky_HuUyt9Ca_Q9rT_4BHU_9tSM_mhRRLnK7Qbct&web_search_code=%7B%22tiktok%22%3A%7B%22client_params_x%22%3A%7B%22search_engine%22%3A%7B%22ies_mt_user_live_video_card_use_libra%22%3A1%2C%22mt_search_general_user_live_card%22%3A1%7D%7D%2C%22search_server%22%3A%7B%7D%7D%7D&webcast_language=en&msToken=JIk50O8QR3_BkPbiMQlOiu14nujJOk40Skwf0UuhbvyMZmLDGDlT5v0AuoD76bPUdN5rLmEetfjSZrNRtlg-dNXJnzMgSgpqMho0sLE4T85ouxre2mAtPTmG-bnbPS9uYh-YMPDyw00Xz0Lm&X-Bogus=DFSzswVO3vsANGyItbEaOELNKBTI&_signature=_02B4Z6wo000012ZIMLwAAIDANLcQpynAo8NmSDQAALyK93"

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
        "Referer": f"https://www.tiktok.com/search?lang=en&q={query}&t=1710030239083",
        "Referrer-Policy": "strict-origin-when-cross-origin",
    }

    with requests.session() as session:
        response = session.get(url, headers=headers)
        as_json = response.json()

        # print(json.dumps(as_json, indent=4))

        # for item in as_json["data"]:
        #     print(item["item"]["desc"])

        # print(json.dumps(as_json["data"][0]["item"], indent=2))

        download_uri = as_json["data"][0]["item"]["video"]["id"]

        return download_uri
