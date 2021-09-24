import requests
import json
from profile_python.networking import Networking

url = "https://api.github.com/users/joaolfp"
url_repo = "https://api.github.com/users/joaolfp/repos"

networking = Networking()
response = networking.request(url_repo)

values = networking.parsing(response)

print(values[0]['owner']['login'])