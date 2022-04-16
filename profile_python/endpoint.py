path = "https://api.github.com/users/"


class Endpoint(object):

    def data(self, user):
        url = path + str(user)
        return url

    def repo(self, user):
        url = path + str(user) + "/repos"
        return url
