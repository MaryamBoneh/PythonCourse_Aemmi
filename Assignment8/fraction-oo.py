
class Fraction():
    def __init__(self, n=0, d=0):
        self.n = n
        self.d = d

    def mul(self, other):
        self.result = Fraction(0, 0)
        self.result.n = self.n * other.n
        self.result.d = self.d * other.d
        return self.result

    def sum(self, other):
        self.result = Fraction(0, 0)
        self.result.n = self.n * other.d + other.n * self.d
        self.result.d = self.d * other.d
        return self.result

    def divide(self, other):
        self.result = Fraction(0, 0)
        self.result.n = self.n * other.d
        self.result.d = self.d * other.n
        return self.result

    def minus(self, other):
        self.result = Fraction(0, 0)
        self.result.n = self.n * other.d - other.n * self.d
        self.result.d = self.d * other.d
        return self.result


numerator1 = int(input('please enter the numerator of first fraction: '))
denominator1 = int(input('please enter the denominator of first fraction: '))

numerator2 = int(input('please enter the numerator of second fraction: '))
denominator2 = int(input('please enter the denominator of second fraction: '))

frcn1 = Fraction(numerator1, denominator1)
frcn2 = Fraction(numerator2, denominator2)

while True:
    select = input(' 1- sum \n 2- minus \n 3- mul \n 4- divide \n 5- exit \n ')
    if select == '1':
        result = frcn1.sum(frcn2)
        print(result.n, '/', result.d)
    elif select == '2':
        result = frcn1.minus(frcn2)
        print(result.n, '/', result.d)
    elif select == '3':
        result = frcn1.mul(frcn2)
        print(result.n, '/', result.d)
    elif select == '4':
        result = frcn1.divide(frcn2)
        print(result.n, '/', result.d)
    else:
        exit()
