import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()

print(data)