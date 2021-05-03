import colorama
from colorama import Fore
colorama.init()


class Actor():
    def __init__(self, name):
        self.name = name

    def show(self):
        print(Fore.WHITE + self.name)
