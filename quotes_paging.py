import requests
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com"
url = "/page/1/" # 변경된 엔드 포인트를 적용하기 위한 변수 

while url:
    response = requests.get(base_url + url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("div.quote")

    for quote in quotes:
        text = quote.select_one("span.text").get_text(strip=True)
        author = quote.select_one("small.author").get_text(strip=True)
        print(f"{text} - {author}")

    next_btn = soup.select_one("li.next > a")
    url = next_btn["href"] if next_btn else None

