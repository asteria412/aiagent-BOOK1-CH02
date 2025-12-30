import requests
import urllib.robotparser

# robots.txt 확인하기 
# url = "https://www.naver.com/robots.txt"
# response = requests.get(url)
# print(response.text)

# robots.txt 자동으로 확인하기 
import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.naver.com/robots.txt")
rp.read()

print(rp.can_fetch("*", "/"))