
class Fraction():
    def __init__(self, n1, d1, n2, d2):
        self.a = {'n': n1, 'd': d1}
        self.b = {'n': n2, 'd': d2}
        self.result = {}

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


numerator1 = int(input('please enter the numerator of first fraction: '))
denominator1 = int(input('please enter the denominator of first fraction: '))

numerator2 = int(input('please enter the numerator of second fraction: '))
denominator2 = int(input('please enter the denominator of second fraction: '))

frcn = Fraction(numerator1, denominator1, numerator2, denominator2)

while True:
    select = input(' 1- sum \n 2- minus \n 3- mul \n 4- divide \n 5- exit \n ')
    if select == '1':
        frcn.sum()
    elif select == '2':
        frcn.minus()
    elif select == '3':
        frcn.mul()
    elif select == '4':
        frcn.divide()
    else:
        exit()