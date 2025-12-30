import urllib.request
import time

url = "https://thumbnews.nateimg.co.kr/view610///news.nateimg.co.kr/orgImg/nn/2025/12/30/202512301032552310_1.jpg"

start = time.time()
urllib.request.urlretrieve(url, "test.jpg")
print(time.time() - start)