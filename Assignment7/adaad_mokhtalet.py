result = {}

def mul(x, y):
    result = {'s': x['s'] * y['s'] - x['m'] * y['m'],
              'm': x['s'] * y['m'] + x['m'] * y['s']}
    print(result['s'], '+', result['m'], 'i')
    
def sum(x, y):
    result = {'s': x['s'] + y['s'], 'm': x['m'] + y['m']}
    print(result['s'], '+',  result['m'], 'i')

def minus(x, y):
    result = {'s': x['s'] - y['s'], 'm': x['m'] - y['m']}
    print(result['s'], '+',  result['m'], 'i')


select = input(' 1- sum \n 2- minus \n 3- mul \n ')

s = int(input('a real: '))
m = int(input('a mohoomi: '))
a = {'s': s, 'm': m}

s = int(input('b real: '))
m = int(input('n mohoomi: '))
b = {'s': s, 'm': m}

if select == '1':
    sum(a, b)
elif select == '2':
    minus(a, b)
elif select == '3':
    mul(a, b)