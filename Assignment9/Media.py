import pytube
import colorama
from Actor import Actor
from colorama import Fore
colorama.init()

class Media():
    def __init__(self, ID, CATEGORY, NAME, YEAR, DIRECTOR, SCORE, URL, INFO, CASTS):
        self.id = ID
        self.category = CATEGORY
        self.name = NAME
        self.year = YEAR
        self.director = DIRECTOR
        self.imdb_score = SCORE
        self.url = URL
        self.info = INFO
        self.cast = CASTS
        
    def show(self):
        print(Fore.LIGHTWHITE_EX +'-------------------------------------------------------------------------------------------------------------')
        print(f"ID: {self.id},  NAME: {self.name}, CATEGORY: {self.category},  YEAR: {self.year},  DIRECTOR: {self.director},  IMDB SCORE: {self.imdb_score}")
        print(Fore.LIGHTWHITE_EX +'-------------------------------------------------------------------------------------------------------------')
        
    def showInfo(self):
        print(Fore.LIGHTWHITE_EX + self.info)
        
    def showCasts(self):
        casts = self.cast.split('-')
        for actor in casts:
            Actor(actor).show()
            
    def download(self):
        pytube.YouTube(self.url).streams.first().download()
        print(Fore.LIGHTGREEN_EX + 'download success!')
    
    
