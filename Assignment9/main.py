import os
import colorama
from colorama import Fore
from Clip import Clip
from Media import Media
from Film import Film
from Series import Series
from Documentary import Documentary

os.system('cls')
colorama.init()


class Main():
    def __init__(self):
        try:
            f = open('Data.csv')
        except Exception as e:
            print("error: ", e)
            exit()

        big_text = f.read()
        parts = big_text.split('\n')
        self.medias = []
        i = 0

        while i < len(parts):
            info = parts[i].split(',')
            if info[1] == 'film':
                self.medias.append(Film(info))
            elif info[1] == 'documentary':
                self.medias.append(Documentary(info))
            elif info[1] == 'clip':
                self.medias.append(Clip(info))
            elif info[1] == 'series':
                self.medias.append(Series(info))
            i += 1

        print(Fore.LIGHTCYAN_EX + 'data loaded! \nwelcome dear user!')
        self.menu()

    def menu(self):
        print(Fore.LIGHTYELLOW_EX + '\n 1- add new media \n 2- search \n 3- edit \n 4- remove \n 5- show media list \n 6- download \n 7- show info \n 8- duration search \n 9- show actors \n 10- save changes and exit')
        user_select = input('please enter the option you want: ')

        if user_select == '1':
            self.addNewMedia()
        elif user_select == '2':
            self.search()
        elif user_select == '3':
            self.edit()
        elif user_select == '4':
            self.remove()
        elif user_select == '5':
            self.showMediaList()
        elif user_select == '6':
            self.download()
        elif user_select == '7':
            self.showInfo()
        elif user_select == '8':
            self.duration_search()
        elif user_select == '9':
            self.showActors()
        elif user_select == '10':
            self.saveAndExit()
        else:
            print('wrong input')


    def addNewMedia(self):
        category = input('enter the category name first\n ( film - clip - documentary - series ): ')
        id = input('id: ')
        name = input('name: ')
        year = input('year: ')
        director = input('director: ')
        score = input('score: ')
        duration = input('duration: ')
        url = input('url: ')
        info = input('info: ')
        casts = input('casts: ')
        genre = input('genre: ')
        episode = input('episode: ')
        subject = input('subject: ')
        company = input('company: ')
        media_info = [id, category, name, year, director, score, duration, url, info, casts, genre, episode, subject, company]
           
        if category == 'film':
           self.medias.append(Film(media_info))
        elif category == 'clip':
            self.medias.append(Clip(media_info))
        elif category == 'documentary':
            self.medias.append(Documentary(media_info))
        elif category == 'series':
            self.medias.append(Series(media_info))
        else:
            print(Fore.RED + 'wrong input')
            
        self.menu()


    def search(self):
        user_input = input('enter NAME of media: ')
        for media in self.medias:
            if media.name == user_input:
                media.show()
                break
        else:
            print(Fore.RED + 'not found')
        self.menu()


    def duration_search(self):
        print(Fore.GREEN + 'Search media with a specific duration')
        first_duration = input('enter first duration with format {00:00}: ')
        first_duration = first_duration.split(':')
        first_duration = [int(i) for i in first_duration]
        sec_duration = input('enter second duration with format {00:00}: ')
        sec_duration = sec_duration.split(':')
        sec_duration = [int(i) for i in sec_duration]
        for media in self.medias:
            if media.category != 'series':
                media_duration = media.duration.split(':')
                media_duration = [int(i) for i in media_duration]
                if media_duration >= first_duration and media_duration <= sec_duration:
                    media.show()
        self.menu()


    def edit(self):
        print(Fore.LIGHTWHITE_EX + '___ editing a media ___')
        name = input('enter name of media that you want to edit: ')
        for media in self.medias:
            if name == media.name:
                if media.category == 'film':
                    media = media.editFilm()
                    break
                elif media.category == 'documentary':
                    media = media.editDocumentary()
                    break
                elif media.category == 'clip':
                    media = media.editClip()
                    break
                elif media.category == 'series':
                    media = media.editSeries()
                    break
                else:
                    print('there is a problem in the data')
                    break
        else:
            print(Fore.LIGHTCYAN_EX + 'not exists')
        self.menu()


    def remove(self):
        print(Fore.LIGHTWHITE_EX + '___ deleting a product ___')
        user_input = input('please enter the name of media or id: ')

        for media in self.medias:
            if user_input == media.name or user_input == media.id:
                print(Fore.LIGHTRED_EX + 'are you sure you want delete this media? \n  y?  n? ')
                yORn = input()
                if yORn == 'y':
                    self.medias.remove(media)
                    break
        else:
            print(Fore.LIGHTCYAN_EX + 'not exists')
        self.menu()


    def showMediaList(self):
        for media in self.medias:
            media.show()
        self.menu()


    def download(self):
        user_input = input('please enter the name of media or id for download: ')
        for media in self.medias:
            if user_input == media.name or  user_input == media.id:
                media.download()
                break
        else:
            print(Fore.RED + 'not exists')
        self.menu()
    

    def showInfo(self):
        user_input = input('please enter the name of media or id for show information: ')
        for media in self.medias:
            if user_input == media.name or  user_input == media.id:
                media.showInfo()
                break
        else:
            print(Fore.RED + 'not exists')
        self.menu()
        
        
    def showActors(self):
        user_input = input('please enter the name of media or id for show information: ')
        for media in self.medias:
            if user_input == media.name or  user_input == media.id:
                media.showCasts()
                break
        else:
            print(Fore.RED + 'not exists')
        self.menu()


    def saveAndExit(self):
        # ___ update csv file ___
        out = open('Data.csv', 'w')
        for media in self.medias:
            out.write(media.id + ',' + media.category + ',' + media.name + ',' + media.year + ',' + media.director + ',' + media.imdb_score + ',' + media.duration + ',' + media.url + ',' +media.info + ',' + media.cast + ',' + media.genre + ',' + media.episode + ',' + media.subject + ',' + media.company)
            if media != self.medias[-1]:
                out.write('\n')
        out.close()
        print(Fore.LIGHTGREEN_EX + 'Thanx! Goodbye')
        exit()


if __name__ == "__main__":
    widget = Main()
