class Endpoint(object):

    def data(self, user):
        url = "https://api.github.com/users/" + str(user)
        return url

    def repo(self, user):
        url = "https://api.github.com/users/" + str(user) + "/repos"
        return url