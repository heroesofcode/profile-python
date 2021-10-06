import unittest
from profile_python.endpoint import Endpoint

class TestEndpoint(unittest.TestCase):

    def test_get_url_data_with_success(self):
        endpoint = Endpoint().data("user")
        assert endpoint == "https://api.github.com/users/user"

    def test_get_url_repo_with_success(self):
        endpoint = Endpoint().repo("user")
        assert endpoint == "https://api.github.com/users/user/repos"

if __name__ == '__main__':
    unittest.main()
