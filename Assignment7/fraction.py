numerator = int(input('please enter the numerator of first fraction: '))
denominator = int(input('please enter the denominator  of first fraction: '))
a = {'n': numerator, 'd': denominator}

numerator = int(input('please enter the numerator of second fraction: '))
denominator = int(input('please enter the denominator  of second fraction: '))
b = {'n': numerator, 'd': denominator}

result = {}

def mul():
    result = {'n': a['n'] * b['n'],
              'd': a['d'] * b['d']}
    print(result['n'], '/', result['d'])

def sum():
    result = {'n': a['n'] * b['d'] + b['n'] * a['d'],
              'd': a['d'] * b['d']}
    print(result['n'], '/', result['d'])

def divide():
    result = {'n': a['n'] * b['d'],
              'd': a['d'] * b['n']}
    print(result['n'], '/', result['d'])

def minus():
    result = {'n': a['n'] * b['d'] - b['n'] * a['d'],
              'd': a['d'] * b['d']}
    print(result['n'], '/', result['d'])
    
    
while True:
    select = input(' 1- sum \n 2- minus \n 3- mul \n 4- divide \n 5- exit \n ')

    if select == '1':
        sum()
    elif select == '2':
        minus()
    elif select == '3':
        mul()
    elif select == '4':
        divide()
    else:
        exit()
