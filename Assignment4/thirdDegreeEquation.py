import math

z = int(input('a: '))
a = int(input('b: '))
b = int(input('c: '))
c = int(input('d: '))

if z != 0:
    a /= z
    b /= z
    c /= z

    p = b - ((a ** 2) / 3)
    q = (2 * ((a ** 3) / 27)) - ((a * b) / 3) + c
    delta = ((q ** 2) / 4) + ((p ** 3) / 27)

    print('delta: ', delta)
    if delta > 0:
        x1 = ((- (q/2) + math.sqrt(delta)) ** 1/3) + \
            ((- (q/2)+math.sqrt(delta))**1/3) - (a/3)
        print('just x1: ', x1)

    elif delta == 0:
        x1 = (-2 * (q/2) ** 1/3) - a/3
        x2 = ((q/2) ** 1/3) - a/3
        print('x1: ', x1, 'x2: ', x2)

    else:
        x1 = (2 / 1.73) * math.sqrt(-p) * math.sin(1/3 * math.sin((3 *
                                                                   math.sqrt(3 * q) / (2 * ((math.sqrt(-p)**3))))) ** -1) - a / 3

        x2 = -(2 / 1.73) * math.sqrt(-p) * math.sin(1/3 * math.sin((3 *
                                                                    math.sqrt(3 * q) / (2 * ((math.sqrt(-p)**3))))) ** -1 + (math.pi / 3)) - a / 3

        x3 = (2 / 1.73) * math.sqrt(-p) * math.cos(1/3 * math.sin((3 *
                                                                   math.sqrt(3 * q) / (2 * ((math.sqrt(-p)**3))))) ** -1 + (math.pi / 6)) - a / 3
        print(' x1: ', x1, '\n x2: ', x2, '\n x3: ', x3)
else:
    print('no answer')
    exit()
