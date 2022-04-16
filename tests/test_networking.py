from profile_python.networking import Networking


def test_request_success():
    json = '["animal","career","celebrity","dev","explicit","fashion","food","history",' \
           '"money","movie","music","political","religion","science","sport","travel"]'

    url = "https://api.chucknorris.io/jokes/categories"
    networking = Networking()
    response = networking.request(url)
    assert response == json


def test_parsing_success():
    url = "https://api.chucknorris.io/jokes/categories"
    networking = Networking()
    response = networking.request(url)

    value = networking.parsing(response)
    assert value[0] == "animal"
