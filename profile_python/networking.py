import requests
import json


class Networking(object):

    def request(self, url):
        try:
            response = requests.get(url)

            if response.status_code == 200:
                return response.text
        except:
            print("Error making request")

    def parsing(self, value):
        try:
            return json.loads(value)
        except:
            print("Error making parsing")
