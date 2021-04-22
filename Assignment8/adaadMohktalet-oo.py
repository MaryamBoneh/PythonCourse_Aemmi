
class AdadMokhtalet():
    def __init__(self, s=0, m=0):
        self.s = s
        self.m = m

    def mul(self, other):
        result = AdadMokhtalet(0, 0)
        result.s = self.s * other.s - self.m * other.m
        result.m = self.s * other.m + self.m * other.s
        return result

    def sum(self, other):
        result = AdadMokhtalet(0, 0)
        result.s = self.s + other.s,
        result.m = self.m + other.m
        return result

    def minus(self, other):
        result = AdadMokhtalet(0, 0)
        result.s = self.s - other.s
        result.m = self.m - other.m
        return result

    def divid(self, other):
        result = AdadMokhtalet(0, 0)
        temp = other.s ** 2 + other.m ** 2
        result.s = (self.s * other.s + self.m * other.m) / temp
        result.m = (self.m * other.s - self.s * other.m) / temp
        return result


s1 = int(input('a real: '))
m1 = int(input('a mohoomi: '))

s2 = int(input('b real: '))
m2 = int(input('b mohoomi: '))

select = input(' 1- sum \n 2- minus \n 3- mul \n  4- divid \n ')

addMkhtlt1 = AdadMokhtalet(s1, m1)
addMkhtlt2 = AdadMokhtalet(s2, m2)

if select == '1':
    result = addMkhtlt1.sum(addMkhtlt2)
    print(result.s, '+', result.m, 'i')

elif select == '2':
    result = addMkhtlt1.minus(addMkhtlt2)
    print(result.s, '+', result.m, 'i')

elif select == '3':
    result = addMkhtlt1.mul(addMkhtlt2)
    print(result.s, '+', result.m, 'i')

elif select == '4':
    result = addMkhtlt1.divid(addMkhtlt2)
    print(result.s, '+', result.m, 'i')
