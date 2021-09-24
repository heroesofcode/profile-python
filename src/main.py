import requests

url = "https://api.github.com/users/joaolfp"
response = requests.get(url)

print(response.text)