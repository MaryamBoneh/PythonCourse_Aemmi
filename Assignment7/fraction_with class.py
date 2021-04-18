import sys
import os

class fraction():
    def __init__(self):
        self.numerator = int(input('please enter the numerator of first fraction: '))
        self.denominator = int(input('please enter the denominator  of first fraction: '))
        self.a = {'n': self.numerator, 'd': self.denominator}

        self.numerator = int(input('please enter the numerator of second fraction: '))
        self.denominator = int(input('please enter the denominator  of second fraction: '))
        self.b = {'n': self.numerator, 'd': self.denominator}

        self.result = {}
        
        while True:
            select = input(' 1- sum \n 2- minus \n 3- mul \n 4- divide \n 5- exit \n ')

            if select == '1':
                self.sum()
            elif select == '2':
                self.minus()
            elif select == '3':
                self.mul()
            elif select == '4':
                self.divide()
            else:
                exit()
    
    
    def mul(self):
        self.result = {'n': self.a['n'] * self.b['n'],
                'd': self.a['d'] * self.b['d']}
        print(self.result['n'], '/', self.result['d'])

    def sum(self):
        self.result = {'n': self.a['n'] * self.b['d'] + self.b['n'] * self.a['d'],
                'd': self.a['d'] * self.b['d']}
        print(self.result['n'], '/', self.result['d'])

    def divide(self):
        self.result = {'n': self.a['n'] * self.b['d'],
                'd': self.a['d'] * self.b['n']}
        print(self.result['n'], '/', self.result['d'])

    def minus(self):
        self.result = {'n': self.a['n'] * self.b['d'] - self.b['n'] * self.a['d'],
                'd': self.a['d'] * self.b['d']}
        print(self.result['n'], '/', self.result['d'])
    

if __name__ == "__main__":
    widget = fraction()
    widget.show()