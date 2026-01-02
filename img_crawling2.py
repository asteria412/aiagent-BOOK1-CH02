import requests
from bs4 import BeautifulSoup
import urllib.request
import time

for section in range(100, 106):
    url = f"https://news.naver.com/section/{section}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    img_list = soup.select(".sa_thumb img")

    for i, img in enumerate(img_list, 1):
        img_url = img.get("src") or img.get("data-src")
        filename = f"images/{section}_{i}.jpg"
        urllib.request.urlretrieve(img_url, filename)

print("다운로드 끝")