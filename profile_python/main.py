import requests
import json
from profile_python.networking import Networking

url = "https://api.github.com/users/joaolfp"
networking = Networking()
response = networking.request(url)

values = networking.parsing(response)

print(values['login'])