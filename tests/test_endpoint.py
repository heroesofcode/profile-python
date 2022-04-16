from profile_python.endpoint import Endpoint


def test_get_url_data_with_success():
    endpoint = Endpoint().data("user")
    assert endpoint == "https://api.github.com/users/user"


def test_get_url_repo_with_success():
    endpoint = Endpoint().repo("user")
    assert endpoint == "https://api.github.com/users/user/repos"
