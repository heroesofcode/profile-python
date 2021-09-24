from profile_python.networking import Networking

url = "https://api.github.com/users/joaolfp"
url_repo = "https://api.github.com/users/joaolfp/repos"

networking = Networking()
response_datas = networking.request(url)
response_repos = networking.request(url_repo)

values_datas = networking.parsing(response_datas)
values_repos = networking.parsing(response_repos)

def get_datas(datas):
    print(datas['login'])
    print(datas['name'])
    print(datas['bio'])
    print(datas['company'])
    print(datas['blog'])
    print(datas['location'])

def get_repos(repos):
    for repo in repos:
        print(repo['name'])

print("1 - My datas")
print("2 - Repositories")

print("-----------------------------------------------")

option = input("Choose an option: ")

if option == "1":
    get_datas(values_datas)
else:
    get_repos(values_repos)