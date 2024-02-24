import os
import requests
import json
import time


def download_images(keyword, save_path, start_page=0, end_page=2, delay=1):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for page in range(start_page, end_page):
        # pn is not page
        # current rn = 30, meaning 30 images per page
        pn = page * 30
        url = f'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={keyword}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word={keyword}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={pn}&rn=30&gsm=1e&1618477640587='
        print(f"page {page}：{url}")
        response = requests.get(url, headers=headers)

        try:
            json_data = json.loads(response.text)
        except json.decoder.JSONDecodeError:
            print(f"page {page} JSON decode error, continuing after {delay} sec")
            # slowdown to prevent blocking
            time.sleep(delay)
        else:
            # get image URL
            img_urls = [img['thumbURL'] for img in json_data['data'] if 'thumbURL' in img]
            # download each image
            for i, url in enumerate(img_urls):
                print(f"download image {i} at page {page} (pn={pn}) from {url}")
                response = requests.get(url)
                with open(os.path.join(save_path, f'{keyword}_{page}_{i}.jpg'), 'wb') as f:
                    f.write(response.content)
            # slowdown to prevent blocking
            time.sleep(delay)