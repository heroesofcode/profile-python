from profile_python.networking import Networking
from profile_python.endpoint import Endpoint
from rich.console import Console
from profile_python.profile import Profile
import pyfiglet


class App(object):
    console = Console()

    ascii_banner = pyfiglet.figlet_format("Profile GitHub")
    print(ascii_banner)

    console.print("🏠 Welcome, write your GitHub user to see their profile and repositories 🔥", style="#FFFF00")
    console.print("✍  João Lucas", style="#FFFF00")
    print("\n")
    user = input("Enter your username: ")

    url_data = Endpoint().data(user)
    url_repo = Endpoint().repo(user)

    networking = Networking()
    response_datas = networking.request(url_data)
    response_repos = networking.request(url_repo)

    values_datas = networking.parsing(response_datas)
    values_repos = networking.parsing(response_repos)

    def run_app(self):
        profile = Profile()
        profile.run_app(self.values_datas, self.values_repos)
