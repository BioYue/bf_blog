from pathlib import Path
import requests
import re

res = requests.get('https://www.bing.com/hp/api/model?mkt=zh-CN')
url_suffix = res.json()['MediaContents'][0]['ImageContent']['Image']['Wallpaper']

match = re.search(r'OHR\.(.*?.jpg)', url_suffix)
bing_bg_name = match.group(1)

img_url = 'https://www.bing.com' + url_suffix
bing_bg_img = requests.get(img_url).content

BASE_DIR = Path(__file__).resolve().parent.parent

with open(BASE_DIR.joinpath(f'app/blog/static/imgs/{bing_bg_name}'), 'wb') as f:
    f.write(bing_bg_img)
