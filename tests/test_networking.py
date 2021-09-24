import unittest
from profile_python.networking import Networking

class TestNetworking(unittest.TestCase):

    def test_request_success(self):
        json = '["animal","career","celebrity","dev","explicit","fashion","food","history",' \
               '"money","movie","music","political","religion","science","sport","travel"]'

        url = "https://api.chucknorris.io/jokes/categories"
        networking = Networking()
        response = networking.request(url)
        assert response == json

    def test_parsing_success(self):
        url = "https://api.chucknorris.io/jokes/categories"
        networking = Networking()
        response = networking.request(url)

        value = networking.parsing(response)
        assert value[0] == "animal"

if __name__ == '__main__':
    unittest.main()
