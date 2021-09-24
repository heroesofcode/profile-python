from profile_python.networking import Networking
from profile_python.endpoint import Endpoint

user = input("Enter your username: ")

url_data = Endpoint().data(user)
url_repo = Endpoint().repo(user)

networking = Networking()
response_datas = networking.request(url_data)
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
elif option == "2":
    get_repos(values_repos)
else:
    print("This option does not exist")