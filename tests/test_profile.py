from profile_python.profile import Profile
from profile_python.networking import Networking
from profile_python.endpoint import Endpoint


def test_get_data():
    url_data = Endpoint().data("joaolfp")

    networking = Networking()
    response_datas = networking.request(url_data)

    values_datas = networking.parsing(response_datas)

    profile = Profile()
    profile.get_datas(values_datas)
    assert values_datas['login'] == "joaolfp"


def test_get_repos():
    url_repo = Endpoint().repo("joaolfp")

    networking = Networking()
    response_repos = networking.request(url_repo)

    values_repos = networking.parsing(response_repos)

    profile = Profile()
    profile.get_repos(values_repos)

    assert values_repos[0]["language"] == "Objective-C"
