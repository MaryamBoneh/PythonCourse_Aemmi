
class AdadMokhtalet():
    def __init__(self, s1, m1, s2, m2):
        self.a = {'s': s1, 'm': m1}
        self.b = {'s': s2, 'm': m2}
        self.result = {}

    def mul(self):
        self.result = {'s': self.a['s'] * self.b['s'] - self.a['m'] * self.b['m'],
                       'm': self.a['s'] * self.b['m'] + self.a['m'] * self.b['s']}
        return self.result

    def sum(self):
        self.result = {'s': self.a['s'] + self.b['s'], 'm': self.a['m'] + self.b['m']}
        return self.result
        
    def minus(self):
        self.result = {'s': self.a['s'] - self.b['s'], 'm': self.a['m'] - self.b['m']}
        return self.result

    def divid(self):
        temp = b['s'] ** 2 + b['m'] ** 2
        self.result = {'s': (b['s'] * b['s'] + b['m'] * b['m']) /
                  temp, 'm': (b['m'] * b['s'] - b['s'] * b['m']) / temp}
        return self.result
        


s1 = int(input('a real: '))
m1 = int(input('a mohoomi: '))

s2 = int(input('b real: '))
m2 = int(input('b mohoomi: '))

select = input(' 1- sum \n 2- minus \n 3- mul \n ')

addMkhtlt = AdadMokhtalet(s1, m1, s2, m2)

if select == '1':
    result = addMkhtlt.sum()
    print(result['s'], '+', result['m'], 'i')
    
elif select == '2':
    result = addMkhtlt.minus()
    print(result['s'], '+', result['m'], 'i')
    
elif select == '3':
    result = addMkhtlt.mul()
    print(result['s'], '+', result['m'], 'i')
    
elif select == '4':
    result = addMkhtlt.divid()
    print(result['s'], '+', result['m'], 'i')
