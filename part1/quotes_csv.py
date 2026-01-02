import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://quotes.toscrape.com"
url = "/page/1/"

with open("quotes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author"])

    while url:
        response = requests.get(base_url + url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.select("div.quote")

        for quote in quotes:
            text = quote.select_one("span.text").get_text(strip=True)
            author = quote.select_one("small.author").get_text(strip=True)
            writer.writerow([text, author])

        next_btn = soup.select_one("li.next > a")
        url = next_btn["href"] if next_btn else None

print("quotes.csv 파일 저장 완료")